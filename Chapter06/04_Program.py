# Write a python program to find whether a given username contains less than 10 character or not.

username = input("Enter the username: ")

if(len(username)> 10):
    print("Username contains more than 10 characters")
else:
    print("Username contains less than or equals to 10 characters")