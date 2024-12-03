# Python program to display the contents of a directory using the os module.

# Import the os module
import os

# Define the directory path to explore
path = '/'

# Fetch the contents of the specified directory
content = os.listdir(path)

# Print the directory contents
print(content)
