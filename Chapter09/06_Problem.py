# Write a program to find out the line number where python is present in log file.


with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes Python is present. Line no: {lineno}")
        break
    lineno += 1

else:
    print("No Python is not present")
        