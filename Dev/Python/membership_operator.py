"""
1.2 opereators exist, in and not in. they exist to check membership in a sequence.
2.they check if a char/substr/value/variable, using for loop, is present in a sequence/string or not.
3.returns True if specified value is present in a sequence, otherwise False.
"""
str = "Sindi"
print('n' in str)
print('indi' in str)
print('I' in str)
print('s' not in str)

list = [1, 10, -1, 0, 17]
print(10 in list)
print(10 not in list)