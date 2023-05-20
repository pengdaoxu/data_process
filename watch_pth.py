import torch
import numpy as np
model = torch.load('resnet50-19c8e357.pth')
# print(model)
for name, param in model.items():
    print(f"Parameter name: {name}, shape: {param.shape}")
a = (model['conv1.weight'])
weight = a.detach().numpy()
print('weight:',model['conv1.weight'])