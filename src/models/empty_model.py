from torch import nn
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