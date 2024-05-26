import torch
x= torch.tensor( [1.0,2.0,3.0] , requires_grad= True)
                                # pytorch will keep track of the operation we perform on this tensorto compute gradients

y = x**3 + x**2 + 1

y.sum().backward()    #the backward function can only be perform on scalars thats why 
                      # we have to do y.sum() pytorch keeps track of the operation we 

print (x.grad)

