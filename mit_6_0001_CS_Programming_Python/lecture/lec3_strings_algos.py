# for loops over strings
s = "demo loops"
for index in range(len(s)):
	if s[index] == 'i' or s[index] == 'u':
		print("There is an i or u")

for char in s:
	if char == 'i' or char == 'u':
		print("There is an i or u")

# while loops and strings
an_letters = "aefhilmnorszAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

i = 0
while i < len(word):
	char = word[i]
	if char in an_letters:
		print("Give me an " + char + "! " + char)
	else:
		print("Give me a " + char + "! " + char)
	i += 1
print("What does that spell?")
for i in range(times):
	print(word, "!!!")


# perfect cube
cube = 27
cube = 8120601
for guess in range(abs(cube) + 1):
	if guess**3 >= abs(cube):
		break

if guess**3 != abs(cube):
	print(cube, 'is not a perfect cube')
else:
	if cube < 0:
		guess = -guess
	print('Cube root of ' + str(cube) + ' is ' + str(guess))


cube = 27
cube = 10000
epsilon = 0.1
guess = 0.0
increment = 0.01
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
	guess += increment
	num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
	print("Failed on cube root of", cube, "with these parameters.")
else:
	print(guess, "is close to the cube root of", cube)


# bisection cube root
cube = 27
cube = 812030
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low) / 2.0
while abs(guess**3 - cube) >= epsilon:
	if guess**3 < cube:
		low = guess
	else:
		high = guess
	guess = (high + low)/2.0
	num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)