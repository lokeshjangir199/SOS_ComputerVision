import torch

x=torch.rand(2,3)
y=torch.rand(2,3)
print(x)
print(y)

z=torch.rand(4,3)
for i in range(4):
    for j in range(3):
        if i<2:
            z[i,j]=x[i,j]
        else:
            z[i,j]=y[i-2,j]


print(z)
        

 