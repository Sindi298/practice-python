#2 operators exist, is and is not. they exist to compare the objects, to see if they are the same objects or not and to see if they share the same memory location.
a = 5 
b = 5

"""
1.in python a variable is aka tag/name.
2.the memory location where the value is stored is aka an object.
3.and the address of the tag/name or of the object is aka as a object ID.
4.Now, instead of creating a new object and a new object ID for tag b, in python if the tags are of the same class
  the objects are reused over and over again by multiple tags. Hence, tag a & b, return True and share the same object ID.
  If tags are of different classes, the objects will not be reused to store a tag of a different class, instead a new 
   object will be created with its own unique object ID for the different tag, with a different class and false will be
  the outcome.

  Therefore the point of Identity operator is to compare the memory address/object id. Thus in print(a is b), the is
  operator is checking if the object id of (a) is the same as the object id of (b)
"""
print(a is b) #will return True if class is the same and if object ID is the same
print(id(a)) #id() function is used to get the object ID of the tag/object
print(id(b))
print(a is not b)

c = 10
d = '10'
print(c is d)
print(id(c))
print(id(d))

#is not = the opposite of is. will return True, if both classes are not the same and object ID's are not the same
print(c is not d)
