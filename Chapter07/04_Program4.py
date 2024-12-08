# Write a python program to find out the sum of the n natural numbers using while loop.

n = int(input("Enter the number: "))
sum = 0
i = 0

while (i <= n):
    sum = sum + i
    i = i + 1

print(sum)