a = 5
b = 4

print(a & b)

#Bitwise operators are used to calculate binary numbers, therefore the numbers above will first be converted to binary
#eg: 8 4 2 1 - add base numbers to get binary numbers
#a = 0 1 0 1
#b = 0 1 0 0
#a&b = 0 1 0 0 = 4 --rules = if both are 1 it will give you 1

print(a | b)
#a|b = 0 1 0 1 = 5 --rules = gives you 1 of both bits are 1 or if one bit is 1, 0 if both bits are 0

print(a ^ b)
#a^b = 0 0 0 1 = 1 --rules = gives you 1 if both bits are different, 0 if both bits are the same

print(~a)
#--rules = not(compliment) will reverse the base. if bit is 1 it will give you 0, if bit is 0 it will give you 1.
#~a = -(5 + 1) = -6 

print(a << 2)
#--rules = << operand will left shift the value(a) by specified bits(2), and you will be gaining bits on the left.
#eg: 32 16 8 4 2 1
#a = 0  0  0 1 0 1
#a << 2 = 0 1 0 1 0 0 = 20

print(a >> 2)
#--rules = << operand will right shift the value(a) by specified bits(2), and the last bits on the right will be lost
#eg: 32 16 8 4 2 1
#a = 0  0  0 1 0 1
#a >> 2 = 0 0 0 0 0 1 = 1