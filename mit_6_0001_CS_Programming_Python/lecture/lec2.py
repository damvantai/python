hi = "hello there"
name = "dam van tai"
greet = hi + name
print(greet)
greeting = hi + " " + name
print(greeting)
silly = hi + (" " + name) * 3
print(silly)


x = 1
print(x)
x_str = str(x)
print("my fav number is", x, ".", "x=", x)
print("my fav number is", x_str + "." + "x=" + x_str)
# print("my fav number is", + x_str + "." + "x=" + x_str)

# input
text = input("Type anything... ")
print(5 * text)
num = int(input("Type a number... "))
print(5 * num)

# conditionals/branching
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
	print("x and y are equal")
	if y != 0:
		print("therefore, x / y is", x / y)
elif x < y:
	print("x is smaller")
elif x > y:
	print("y is smaller")
print("thanks!")

# remainder
num = int(input("Enter a number: "))
if num % 2 == 0:
	print("number is even")
else:
	print("number is odd")


# while loops
n = input("You are in the Lost Forest\n")
while n == "right" or n == "Right":
	n = input("You are in the Lost Forest\n")
print("\nYou got out of the Lost Forest!\n\o/")

n = 0
while n < 5:
	print(n)
	n = n + 1

# for loops
for n in range(5):
	print(n)

mysum = 0
for i in range(10):
	mysum += 1

print(mysum)

mysum = 0

for i in range(7, 10):
	mysum += i
	if mysum == 5:
		break
		mysum += 1
print(mysum)

# perfect squares
ans = 0
neg_flag = False
x = int(input("enter an integer: "))
if x < 0:
	neg_flag = True
while ans**2 < x:
	ans = ans + 1
if ans**2 == x:
	print("Square root of", x, "is", ans)
else:
	print(x, "is not a perfect square")
	if neg_flag:
		print("Just checking ... did your mean", -x, "?")