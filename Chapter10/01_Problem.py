# Create a class programmer for storing information of few programmers working at microsoft.

class programmer():
    company = "Microsoft" # This is class attribute
    Salary = 2000000      # This is class attribute
    Profile = "Software Engineer" # This is class attribute

vishal = programmer()
vishal.name = "vishal" # This is instance attribute
print(vishal.name, vishal.company, vishal.Salary, vishal.Profile )