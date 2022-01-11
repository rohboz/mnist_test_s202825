from torch import nn
from torch.nn.modules import loss
from torch.utils.data import DataLoader

data = DataLoader([1,2,3,4])
print(isinstance(data, DataLoader))
los = nn.L1Loss()
print(type(los))
print(isinstance(los, nn.Module))
#print(isinstance(loss, nn.modules.loss))