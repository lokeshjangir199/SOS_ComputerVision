import torch

a= torch.rand(3,3)
print(a)

print(a.mean())
std_dev = torch.std(a)
print(std_dev)

print(torch.std(a , correction=False)) # same as i calculated manually
