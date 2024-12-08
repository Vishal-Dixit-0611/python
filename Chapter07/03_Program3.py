# Write a program to find whether the number a given number is prime or not.

# Prime Numbers = The numbers which are divided by 1 and itself are the prime numbers.

num = int(input("Enter the number: "))

for i in range(2, num):
    if(num % i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime") 