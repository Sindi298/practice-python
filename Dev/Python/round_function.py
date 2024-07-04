'''
1. round function is used to round off the numbers.
2. general syntax includes 2 parameters/arguments: eg: round(number, no. of digits)
3. the forst argument is compulsory, it the number you want ot round off.
4. the 2nd argument is optional & is how many digits you want to round the number to.
   the no. of digits can be pstve, zero or negtve
5. when the no. of digits is a negtve number. the number represented will indicate the number it will be rounded off too. eg: 
   round(674,-1) = -1 will indicate that the last no, will be a zero,
   and the remaining digits will need to to be rounded up or down according to the last number(in this case 4)
   therefore the answer will be 670.
'''

round(21.33333, 2)
print(round(21.33333,2))
print(round(7))
print(round(7,2))
print(round(7.62))
print(round(67.56789,2))
print(round(67.6657, 0))
print(round(7.5))#it will return the nearest even number
print(round(6.5))#it will return the nearest even number
print(round(674, -1))
'''
6. the above rule will be applied if the no. of digits increases eg: (-2)
   eg: round(674, -2) = -2 will indicate that the last 2 numbers will be zeros
   and the remaining digit will be rounded up or down to the nearest hundred according 
   to the number next to it, in this case it will be 700.
'''
print(round(674, -2))
'''
eg: round(674, -3) = -3 
7. the above rule will also be applied if the no. of digits increases to eg: (-3),
   even if the given number only has 3 digits -3 will indicate that the last 3
	numbers will be zeros and the remaining digit will be rounded up or down to 
   the nearest 1000. because there are no numbers left, zero is automatically applied,
   in this case the zero will be rounded up to 1, and the answer will be 1000.
   '''
print(round(674, -3))
print(round(-8/3))#you can also round off fractions
print(round(-1.5))
print(round(-8/3, 2))