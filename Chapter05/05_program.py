# create an empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as their names. Assume that the names are unique.

dict = {}

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
dict.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
dict.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
dict.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
dict.update({name: lang})

print(dict)