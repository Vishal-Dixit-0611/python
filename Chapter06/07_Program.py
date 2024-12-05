# Write a python program to find out whether a given post is talking about "Vishal" or Not

post = input("Enter the post: ")
comment = "Vishal"

if (comment.lower() in post.lower()):
    print("Comment is present in post")
else:
    print("Comment is not present in post")
