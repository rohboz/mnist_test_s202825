# dataset = MNIST(...)
# assert len(dataset) == N_train for training and N_test for test
# assert that each datapoint has shape [1,28,28] or [728] depending on how you choose to format
# assert that all labels are represented

import torch
from __init__ import _PATH_DATA
filepath = _PATH_DATA+"/processed/"
train = torch.load(filepath + "trainset.pt")
test = torch.load(filepath + "testset.pt")

assert train[:][0].shape == torch.Size([25000, 28, 28])
assert train[:][1].shape == torch.Size([25000])
assert torch.all(train[:][1].unique() == torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

assert test[:][1].shape == torch.Size([5000])
assert test[:][0].shape == torch.Size([5000, 28, 28])
assert torch.all(test[:][1].unique() == torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))