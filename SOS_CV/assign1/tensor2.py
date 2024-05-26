import torch

x= torch.rand(5,3)
print(x)

#the transpose of x is a

a= torch.rand(3,5)


for i in range(5):
    for r in range(3):
        a[r,i]=x[i,r]


print(a)

