# A spam comment is defined as a text containing the following keywords:
'''
"make a money lot"
"buy now"
"subscribe this"
"click here"
'''
# Write a program to detect these spam

comment1 = "make a money lot"
comment2 = "buy now"
comment3 = "subscribe this"
comment4 = "click here"

post = input("Enter the comment: ")

if((comment1 in post) or (comment2 in post) or (comment3 in post) or (comment4 in post)):
    print("Comment is spam")
else:
    print("Comment is not spam")