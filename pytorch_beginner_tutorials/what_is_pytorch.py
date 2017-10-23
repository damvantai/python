from __future__ import print_function

import torch
import numpy as np

x = torch.Tensor(5, 3)
print("x: {}".format(x))

# Construct a randomly initialized matrix
x = torch.rand(5, 3)
print("x: {}".format(x))

# Get its size
print(x.size())

# Operations
y = torch.rand(5, 3)

print("y: {}".format(y))

print(x + y)

print(torch.add(x, y))

result = torch.Tensor(5, 3)
torch.add(x, y, out=result)
print("result: {}".format(result))

# adds x to y
y.add_(x)
print("y = y + x {}".format(y))

x.copy_(y)
print(x)

# begin from 0 index
print(x[:, 1])

# Converting torch Tensor to numpy Array
a = torch.ones(5)
print(a)

b = a.numpy()
print(b)

a.add_(1)
print(a)
print(b)

# Converting numpy Array to torch Tensor
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)


# CUDA Tensors
print("CUDA Tensors")
if torch.cuda.is_available():
	x = x.cuda()
	y = y.cuda()
	x + y
