import os

import matplotlib.pyplot as plt
import torch
import torch.nn.functional as F
from torch import nn, optim

filepath = "data/processed/"
outpath = "models/trained_models/"
train = torch.load(filepath + "trainset.pt")

train_set, val_set = torch.utils.data.random_split(train, [24000, 1000])
valloader = torch.utils.data.DataLoader(val_set, batch_size=1000, shuffle=True)
trainloader = torch.utils.data.DataLoader(train_set, batch_size=64, shuffle=True)

model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Dropout(0.25),
    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Dropout(0.25),
    nn.Linear(128, 64),
    nn.ReLU(),
    nn.Dropout(0.25),
    nn.Linear(64, 10),
    nn.LogSoftmax(dim=1),
)

criterion = nn.NLLLoss()
optimizer = optim.Adam(model.parameters())
epochs = 20
Trn_loss = []
Val_loss = []
for e in range(epochs):
    running_loss = 0
    for images, labels in trainloader:
        # Flatten MNIST images into a 784 long vector
        images = images.view(images.shape[0], -1)

        # TODO: Training pass
        optimizer.zero_grad()
        output = model(images.float())
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
    else:
        Trn_loss.append(running_loss / len(trainloader))
        print(f"Training loss: {Trn_loss[-1]}")
        # Flatten MNIST images into a 784 long vector
        images, labels = next(iter(valloader))
        images = images.view(images.shape[0], -1)
        # TODO: Validation pass
        optimizer.zero_grad()
        output = model(images.float())
        loss = criterion(output, labels)
        Val_loss.append(loss.item())
        print(f"Validation loss: {Val_loss[-1]}")


os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

X = range(len(Trn_loss))
plt.plot(X, Trn_loss)
plt.plot(X, Val_loss)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend(["Training Loss", "Validation Loss"])
plt.savefig("reports/figures/model.png")

torch.save(model.state_dict(), outpath + "model.pt")
