# class Point:
# 	def __init__(self, x, y):
# 		self.move(x, y)

# 	def move(self, x, y):
# 		self.x = x
# 		self.y = y

# # a = Point()
# b = Point(1, 2)
# print(b.x, b.y)


# Python function use to provide default arguments


class Point:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def move(self, x, y):
		self.x += x
		self.y += y

a = Point()
b = Point(1)
# c = Point(,1)
d = Point(1, 2)
print(a.x, a.y)
print(b.x, b.y)
a.move(1, 3)
b.move(1, 2)

print(a.x, a.y)
print(b.x, b.y)
print(d.x, d.y)


0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0
1 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 0
1 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 0
0 & 0 & 1 & 0 & 1 & 1 & 0 & 0 & 0
0 & 0 & 0 & 1 & 0 & 1 & 1 & 0 & 0
0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0
0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 1
0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 1
0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 0