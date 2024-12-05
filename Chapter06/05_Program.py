# Write a python program to find out whether a given name is present in a list or not.

names = ["Vishal", "Muskan", "Jerry", "Sunny", "Honey"]

name = input("Enter the name you want to search: ")

if(name in names):
    print(name, "is present")

else:
    print(name, "is not present")