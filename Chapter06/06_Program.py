# Write a program to calculate the grade of a student from his marks from the following scheme:
"""
90 - 100 ----> Ex
80 - 90 -----> A
70 - 80 -----> B
60 - 70 -----> C
50 - 60 -----> D
< 50 --------> Fail
"""

sub1 = int(input("Enter marks of sub1 here: "))
sub2 = int(input("Enter marks of sub2 here: "))
sub3 = int(input("Enter marks of sub3 here: "))

grade = ((sub1 + sub2 + sub3) / 300) * 100

print(grade)

if(grade >= 90 and grade <= 100):
    print("Ex")
elif(grade >= 80 and grade < 90):
    print("A")
elif(grade >= 70 and grade < 80):
    print("B")
elif(grade >= 60 and grade < 70):
    print("C")
elif(grade >= 50 and grade < 60):
    print("D")
else:
    print("Fail")
