 #
 #/ = float division - answer will always be a float value in python eg: print(4 / 2) = 4.2
 #// = int division - answer will always be a int value in python eg: print(4 // 2) = 2
 #** = power to - used to calculate base to the power to eg: print(2 ** 3) = 8, print(4 ** 2) = 16

 #precedence rules : 1 = highest, 4 = lowest
 #1.()
 #2.** = R -> L
 #3.* / // % = L -> R
 #4.+ - = L -> R

print(4 / 2)
print(4 // 2)
print(2 ** 3)
print(5 + 2 * 3 - 1 + 10 / 5)

weight = int(input("enter weight in kg: "))
height = float(input("enter height in m: "))

BMI = weight/(height**2)

print("Body mass index is: ",BMI)