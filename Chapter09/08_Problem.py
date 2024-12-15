# Write the program to find out whether a file is identical and matches the content of another file.

with open("this.txt") as f:
    content = f.read()

with open("this2.txt") as g:
    content2 = g.read()

if(content == content2):
    print("Both files are identical")
else:
    print("Files are not identical")
