import torch
from torchsummary import summary
state_dict = None
state_dict = torch.load('src\checkpoints\pifuhd.pt',map_location=torch.device('cpu'))
# print(state_dict['opt'])
# print(state_dict)
for i in state_dict:
    print(i)

for i in state_dict['model_state_dict']:
    print(i)