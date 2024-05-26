import torch

x=torch.rand(2,2)
y=torch.rand(2,2)

print(x)
print(y)
#method 1
a=x*y
print(a)

#method 2
b = torch.rand(2,2)
for i in range(2):
    for j in range(2):
        b[i,j]= x[i,j]*y[i,j]
print(b)

#method 3
c= torch.mul(x,y)
print(c)