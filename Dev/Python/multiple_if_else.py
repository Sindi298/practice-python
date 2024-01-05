height = int(input("enter height in feet "))
bill = 0

if(height >= 3):
	print("can ride")

	age = int(input("what is your age? "))
	if (age < 12):
		bill = 150
		print("Ticket price is R150")
	elif age <= 18:
		bill = 250
		print("Ticket price is R250")
	else:
		bill = 500
		print("Ticket price is R500")

	photo = input("Do you want to take a photo(Y/N)? ")
	if photo == 'y' or photo == 'Y':
		bill = bill + 50

	print(f"Your total bill is R{bill}")

else:
	print("Can't ride")
print("bye")