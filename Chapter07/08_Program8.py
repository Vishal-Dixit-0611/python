# Write a python program to print the following star pattern

'''
*****
*   *
*   *
*   *
*****
'''

n = int(input("Enter the number: "))
i = 1
while(i <= n):
    if (i == 1 or i == n):
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")
    i += 1
    




    