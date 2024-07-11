'''
general syntax of for loop in python =
for tag_name in sequence:
	statement(s)
'''

name = ['Happy New Year', 'sindi'] #this is a list
for i in name:
	print(i)
	if i == 'sindi':
		print("hey, it's me!")

numbers = [2, 3, 4, 5, 6, 7, 8, 9]
squares = []
for p in numbers:
	square = p ** 2
	squares.append(square)
print("The list of squares is:", squares) #this is outside of the for loop, because its not indented.