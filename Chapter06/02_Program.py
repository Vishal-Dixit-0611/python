# Write a program to find out whether a student is passed or fail, if it requires total 40% and atleast 33%, in each subject to pass. Assume 3 Subjects and take marks as an input from the user.


sub1 = int(input("Enter marks of sub1 here: "))
sub2 = int(input("Enter marks of sub2 here: "))
sub3 = int(input("Enter marks of sub3 here: "))

total_percentage = ((sub1 + sub2 + sub3) / 300) * 100

if(total_percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print("Student Passed")
else:
    print("Student Failed")

print("Total percentage is: ", total_percentage)