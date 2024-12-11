# Write a python program using function to find the greatest of three numbers.

def greatest(a, b, c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    else:
        return c
    

print(greatest(11, 22, 3))