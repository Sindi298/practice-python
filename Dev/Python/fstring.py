name = 'Holly'
age = 26
height = 5.7

#the method below is too tedious, especially if you have a lot of tags.
print("My name is: ", name, "I am ", age, "years old", "my height is ",height, "meters")
# if you use (,) instead of (+) then you don't have to typecast

print(f"my name is {name}, I am {age} years old, my height is {height} meters")

print(f"my name is {name}, I am {age} years old, my height is {height} meters")
print(f"my name is {name}, and i am a student")
'''
Q: WAP to find out how many days, weeks, months
we have left, if we live until 90 years old?
'''
days = 365
weeks = 52
months = 12 
life_expectancy = 90
years = life_expectancy-age

age = int(input("enter your current age: "))

print(f"you have {years*days} days, {years*weeks} weeks and {years*months} months left to live")

 