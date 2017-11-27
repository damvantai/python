# import math
# class Point:
# 	pass

# p1 = Point()
# p2 = Point()

# p1.x = 5
# p1.y = 4

# print(p1)

# print(p1.x)

class Point:
	def reset(self):
		self.x = 0
		self.y = 0

p = Point()
p.reset()
print(p.x, p.y)