height = float(input("enter height in meters "))

if(height >= 1.5):
	print("can ride, Please buy token")

	age = int(input("what is your age? "))
	if (age < 12):
		print("Please pay R150")
	elif age <= 18:
		print("Please pay R250")
	else:
		print("Please pay R500")

else:
	print("Can't ride, Sorry, See you next time!")
print("Bye!")