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
<<<<<<< HEAD
=======

# Gradients
out.backward()

# print gradients d(out)/dx
print(x.grad)

x = torch.randn(3)
x = Variable(x, requires_grad=True)

print(x)
y = x * 2
print("y")
print(y)
while y.data.norm() < 2000:
	y = y * 2
	print('--')
	print(y)

print(y)

# gradients = torch.FloatTensor([0.1, 1.0, 0.0001])
# print(gradients)
# y.backward(gradients)
# print(x.grad)

# print(x.grad)

y.backward(torch.Tensor([1.0]))
print(x.grad)
>>>>>>> pytorch
