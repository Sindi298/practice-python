'''
general syntax =
for tag_name in square:
	statement(s)
else:             --rules: control will only go to else condition and be executed, if for loop has completed successfully
	statement(s)  
'''

numbers = [2,3,5,-1,0,53]
for i in numbers:
	print(i)
	if i == 0:
		break;  #for loop has not been successful, because of the use of break
else:
	print("successfully completed!") #control will not go to else condition, as the program has ended
print("out of for/else")


tuple1 = (2,56,34,3,5,-1)
for i in tuple1:
	print(i)
else:
	print("loop successfully completed and we are in else block now!!")


heights = input("enter all heights seperated by a space:")
#151 152 153 154 155 160
height_list = heights.split()

count = 0
for numbers in height_list:
	count = count + 1
print(count)

for i in range(count):
	height_list[i] = int(height_list[i])

total = 0
for person in height_list:
	total += person
avg = total/count
print(round(avg))

#print(height_list)