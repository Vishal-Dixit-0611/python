# Write a python program to find the greatest Number entered by the user.

number1 = int(input("Enter the Number 1: "))
number2 = int(input("Enter the Number 2: "))
number3 = int(input("Enter the Number 3: "))
number4 = int(input("Enter the Number 4: "))



if (number1 > number2 and number1 > number3 and number1 > number4):
    print("Number1 is Greatest Number")

elif(number2 > number1 and number2 > number3 and number2 > number4):
    print("Number2 is Greatest Number")

elif(number3 > number1 and number3 > number1 and number3 > number4):
    print("Number3 is Greatest Number")

else:
    print("Number4 is Greatest Number")

