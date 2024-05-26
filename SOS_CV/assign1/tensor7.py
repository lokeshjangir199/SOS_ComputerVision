import torch

a= torch.rand(2,3)
b= torch.rand(3,4)
print(a)
print(b)

z= a.matmul(b)
print(z)

