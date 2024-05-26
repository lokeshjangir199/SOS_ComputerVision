import torch

x= torch.rand(4,4)

print(x)


for i in range(4):
    for j in range(4):
        if x[i,j] < 0.5:
            x[i,j]=0

print(x)
        