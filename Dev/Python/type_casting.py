length = len ("Sindi Msubo") #len function is used to calculate the length of a string only. falls under TypeError
print("your name has " +str(length) + " characters") #the class length has to be changed to a string class first, because you can't concat 2 different class types

print(type(length))

new_len = str (length)
print(type(new_len))

#to convert string numbers into int
print("10" + " 10")
print(int("10") + int("10"))

#to conver string number to float
print(10 + float("10"))
"""
this will give ValueError
name = "sindi" 
print(10 + int(name))

"""
user1 = input ("input your number: ") #anything collected from input function is considered as string
user2 = input (" input your number: ")

total = (int(user1) + int(user2)) #you need to convert your string inputs into int classes
print(total)