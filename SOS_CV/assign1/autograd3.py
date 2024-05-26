import torch
x= torch.tensor([2.0,3.0] ,requires_grad= True)
y= torch.tensor([4.0,5.0] ,requires_grad= True)

z = x*y
print(z)

z.sum().backward()
print(x.grad)
print(y.grad)