order = str(input("do you want delivery or collect?"))

bill = 0
s_pepperoni = 30
m_pepperoni = 50
l_pepperoni = 70
cheese = 20

if(order == "delivery"):
	print("proceed online order")

	pizza = str(input("enter size of pizza: "))
	if (pizza == "small"):
		bill = 100
		print(f"Small pizza cost R{bill}")

	elif pizza == "medium":
		bill = 200
		print(f"Medium pizza cost R{bill}")
		
	else:
		bill = 300
		print(f"Large pizza cost R{bill}")

	toppings = input("Do you want Pepperoni on your pizza(Y/N)?")
	while toppings == 'y' or toppings == 'Y':
		if pizza == "small":
			pepperoni = (bill + s_pepperoni)
			print(f"Pepperoni for small pizza cost R{s_pepperoni}")
			print(f"Cost of pizza is now R{pepperoni}")

		elif pizza == "medium":
			pepperoni = (bill + m_pepperoni)
			print(f"Pepperoni for medium pizza cost R{m_pepperoni}")
			print(f"Cost of pizza is now R{pepperoni}")

		else:
			pepperoni = (bill + l_pepperoni)
			print(f"Pepperoni for large pizza cost R{l_pepperoni}")
			print(f"Cost of pizza is now R{pepperoni}")
		break;

	p_extra_cheese = input("Do you want extra cheese with your pepperoni pizza(Y/N)? ")
	while p_extra_cheese == 'y' or p_extra_cheese == 'Y':
		if pizza == "small":
			everything = (bill + s_pepperoni + cheese)
			print(f"Cost of extra cheese is R{cheese}")
			print(f"Your total bill is R{everything}")

		elif pizza == "medium":
			everything = (bill + m_pepperoni + cheese)
			print(f"Cost of extra cheese is R{cheese}")
			print(f"Your total bill is R{everything}")

		else:
			everything = (bill + l_pepperoni + cheese)
			print(f"Cost of extra cheese is R{cheese}")
			print(f"Your total bill is R{everything}")
		break;

	extra_cheese = input("Do you want extra cheese with your pizza(Y/N)? ")
	while extra_cheese == 'y' or extra_cheese == 'Y':
		if pizza == "small":
			plain = (bill + cheese)
			print(f"Cost of extra cheese is R{cheese}")
			print(f"Your total bill is R{plain}")

		elif pizza == "medium":
			plain = (bill + cheese)
			print(f"Cost of extra cheese is R{cheese}")
			print(f"Your total bill is R{plain}")

		else:
			plain = (bill + cheese)
			print(f"Cost of extra cheese is R{cheese}")
			print(f"Your total bill is R{plain}")

		break;
else:
	print("sorry! order must be made at the store, goodbye!")