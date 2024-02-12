import sys
# Primitive Data Types
# 1. int  2. float  3. boolean  4. string
# String
print("Supragya"[0])
print("Supragya"[1])
print("Supragya"[-1])
print(sys.getsizeof("Supragya"))
# default size of character is 50 bytes then 1 byte for each character

# String Slicing
print("Supragya"[0:3])
print("Supragya"[0:7])
print("Supragya"[0:8]) 
print(type("Supragya"))

# String Repetition
print("Supragya"*3)

# Integer
print(123 + 345)
print(123_456_789)
print(type(123_456_789))
print(sys.getsizeof(123))
# default size of int is 28 bytes
# size of int is not limited in python

# Float
print(3.14159)
print(3.1_4159)
print(type(3.14159))
print(sys.getsizeof(3.19))
# default size of float is 24 bytes
# size of float is not limited in python

# Boolean
print(True)
print(False)
print(type(True))
print(type(False))
print(sys.getsizeof(True))
# default size of boolean is 28 bytes