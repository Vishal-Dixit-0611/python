# Write a python function which converts inches to cms.

# There are 2.54 cm in 1 inch.

inches = int(input("Enter the length into inches: "))

def inch_2_cms(inches):
    cms = inches * 2.54
    return cms

print(inch_2_cms(inches),"cms")