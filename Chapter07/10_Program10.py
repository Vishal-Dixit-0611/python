# Print the following pattern using python using for and while loop.
'''
* * * * * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 


* * * * * 
  * * * 
    *
'''

n = int(input("Enter the number: "))

# Using for loop
for i in range(1, n+1):   
    if(i == 1):
        print("*"*(2*n-1))
    else:
        print(" "*(i-1) + "*"*(2*n -(2*i-1)))

# Using while loop
i=1
while(i <= n):
    if(i == 1):
        print("*"*(2*n-1))
    else:
        print(" "*(i-1) + "*"*(2*n -(2*i-1)))
    i += 1
