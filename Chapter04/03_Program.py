# Check that a tuple can't be changed in python.

tuple = (1, 2, 3, 4, 5)

print(tuple[2])
tuple[2] = 33 # 'tuple' object does not support item assignment means tuple is immutable 
print(tuple[2])