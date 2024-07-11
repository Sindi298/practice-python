#there are 11 list methods/functions in python--read up on them
'''
append()---	Adds an element at the end of the list
clear()---	Removes all the elements from the list
copy()---	Returns a copy of the list
count()---	Returns the number of elements with the specified value
extend()---	Add the elements of a list (or any iterable), to the end of the current list
index()---	Returns the index of the first element with the specified value
insert()---	Adds an element at the specified position
pop()---	Removes the element at the specified position
remove()---	Removes the item with the specified value
reverse()---Reverses the order of the list
sort()---	Sorts the list
max()---
min()---
len()---
---------------------------------------------------------------------------------------------------
'''

#The append() method appends an element to the end of the list.
#syntax == list.append(elmnt)
#######################################################################

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)		#we are appending b to a & b will be added to a as a whole list.
print(a)

numbers = [2, 3, 4, 5, 6, 7, 8, 9]
squares = []
for p in numbers:
	square = p ** 2
	squares.append(square)
print("The list of squares is:", squares) #this is outside of the for loop, because its not indented.

#####################################################################################################

#The clear() method removes all the elements from a list. - NB: it takes no arguments
#syntax == list.clear()
#Q:Remove all elements from the fruits list
############################################################

groceries = ['apple', 'banana', 'cherry', 'orange']
groceries.clear()
print(groceries)

###########################################################

#The copy() method returns a copy of the specified list. - NB: it takes no arguments
#syntax == list.copy()
#Q:Copy the fruits list:
###########################################################

groceries = ['apple', 'banana', 'cherry', 'orange']
duplicate = groceries.copy()
print(duplicate)

#############################################################

#The count() method returns the number of elements with the specified value. NB: it takes arguments
#list.count(value)
#Q:Return the number of times the value "cherry" appears in the fruits list:

fruits = ['apple', 'banana', 'cherry']
x = fruits.count('cherry')
print(x)
#Return the number of times the value 9 appears in the list:

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

############################################################

#The extend() method adds the specified list elements (or any iterable) to the end of the current list.
#syntax == list.extend(iterable) NB: argument needed
#Q:add the elements of cars to the fruits list:

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

#Q: add a tuple to the fruits list:

fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

###########################################################

#The index() method returns the position at the first occurrence of the specified value. NB: argument needed
#syntax == list.index(elmnt)
#Q:what is the position of the value cherry:

fruits = ['apple', 'banana', 'cherry']
x = fruits.index('cherry')
print(x)

#Q:what is the position of the value 32
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x) #Note: The index() method only returns the first occurrence of the value.

################################################################################

#The insert() method inserts the specified value at the specified position.
#syntax == list.insert(pos, elmnt)
#Q:Insert the value "orange" as the second element of the fruit list:

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')
print(fruits)

#######################################################################################

#The pop() method removes the element at the specified position.
#syntax == list.pop(pos)
#Q:Remove the second element of the fruit list:

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

#Q: return the removed element:

fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x) #Note: The pop() method returns removed value.

#########################################################################

#The remove() method removes the first occurrence of the element with the specified value.
#syntax == list.remove(elmnt)
#Q: Remove the "banana" element of the fruit list:

fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits)

###############################################################################################################################

#The reverse() method reverses the sorting order of the elements.
#syntax == list.reverse()
#Q: Reverse the order of the fruit list:

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

#################################################################################

#The sort() method sorts the list ascending by default.You can also make a function to decide the sorting criteria(s)
#syntax == list.sort(reverse=True|False, key=myFunc)
#reverse--Optional. reverse=True will sort the list descending.Default is reverse=False
#key--Optional. A function to specify the sorting criteria(s)

#Q: sort the list alphabetically:
cars = ['Ford', 'BMW', 'Audi']
cars.sort()
print(cars)

#Q: Sort the list descending:
cars = ['Ford', 'BMW', 'Audi']
cars.sort(reverse = True)
print(cars)

#Q: Sort the list by the length of the values:

def myFunc(a):
	return len(a)

cars = ['Ford', 'BYD', 'BMW', 'Audi', 'Haval']
cars.sort( key = myFunc)
print(cars)