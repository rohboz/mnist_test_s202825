import sys
print(sys.path)
sys.path.append('')
print(sys.path)

from src.models.empty_model import model
from __init__ import _PATH_MODEL
import torch


model.load_state_dict(torch.load(_PATH_MODEL+'\\trained_models\\model.pt'))
test_input = torch.rand((1,784))
with torch.no_grad():
    logps = model(test_input.float())
assert logps.shape == torch.Size([1,10])

