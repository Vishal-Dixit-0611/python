# Write a python program using function to convert celcius to fahrenheit.

c = int(input("Enter the temperature in Celcius: "))

def c_2_f(c):
    return (c * 9/5) + 32
print(f"The value is",c_2_f(c),"°F")
