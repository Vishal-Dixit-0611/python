# Write a python program to print the following pattern:

'''
*
**
***
****
*****
'''

n = int(input("Enter the number: "))

for i in range(1, n+1):
    print("*"*i, end="")
    print( )