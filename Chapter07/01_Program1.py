# Write a python program to print multiplication table of a given number using for and while loop.

n = int(input("Enter the number: "))

# Using for Loop
for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")



# Using while loop
i =1
while(i <= 10):
    print(f"{n} X {i} = {n * i}")
    i += 1
