# Write a python function to print first n lines of the following pattern:

'''
*****
****
***
**
*

n=5
for i in range(0, n):
    print("*"*(n-i),end="")
    print(" "*i)
'''

def pattern(n):
    # for i in range(0, n):
    #     print("*"*(n-i),end="")
    #     print(" "*i)
    
    i = 0
    while(i < n):
        print("*"*(n-i),end="")
        print(" "* i)
        i += 1
        

n = int(input("Enter the number: "))

pattern(n)