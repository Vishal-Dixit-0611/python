# Write a program to wipe out the content of a file using python.



with open("this2.txt") as f:
    content = f.read()

with open("this2.txt", "w") as g:
    g.write(" ")