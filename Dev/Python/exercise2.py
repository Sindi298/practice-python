numbers = input("enter list of numbers seperated by a space:")
#20 30 40 50 -5 37 0 -9
numbers_list = numbers.split() #use the split function to split the numbers. split numbers will be stored in var akanumbers_list
#numbers are printed in inverted commas, meaning they are a string literals
#use for loop with range to change split numbers from string to int
#if you are not using the function len(), you have to first calculate the list of numbers from input
count = 0 
for number in numbers_list:#for loop to assign each split number an index and be able to count them
	count += 1
print(f"length of list is {count}")

for i in range(count):
	numbers_list[i] = int(numbers_list[i])

maximum_num = numbers_list[0]#we are assuming the max number is at index 0. this must be included
for number in numbers_list:
	if number > maximum_num:
		maximum_num = number
print(f"the max number is : {maximum_num}")