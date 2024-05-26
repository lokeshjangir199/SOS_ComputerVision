import torch

x= torch.tensor([1.0] , requires_grad=True)
y= torch.tensor([2.0], requires_grad= True)

#let  g(x,y) = z

z=(x**2)*y + y**3

z.backward()
print(x.grad)
print(y.grad)