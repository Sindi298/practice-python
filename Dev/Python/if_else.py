height = int(input("enter height in meters "))

if(height >= 3):
	print("can ride")

	age = int(input("what is your age? "))
	if (age < 12):
		print("Please pay R150")
	elif age <= 18:
		print("Please pay R250")
	else:
		print("Please pay R500")

else:
	print("Can't ride")
print("bye")