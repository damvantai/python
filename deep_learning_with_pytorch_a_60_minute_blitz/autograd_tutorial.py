from torch.autograd import Variable

import torch

x = Variable(torch.ones(2, 2), requires_grad=True)
print(x)

y = x + 2
print(y)

# y was created as a result of an operation, so it has a grad_fn
print(y.grad_fn)

# do more operations on y
z = y * y * 3
out = z.mean()

print(z, out)
