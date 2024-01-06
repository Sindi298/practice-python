for number in range(1,16):
	if number % 3 == 0 and number % 5 == 0:#put the if condition that takes both numbers to be divided by at the top, and program will run that fist.
		print("Fizzbuzz")
	elif number % 3 == 0:
		print("Fizz")
	elif number % 5 == 0:
		print("Buzz")
	
	else:
		print(number)