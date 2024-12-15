# Write a program to read the text from a given file 'poem.txt' and find whether it contains the word 'twinkle'

word = input("Enter the word: ")

st = open("poem.txt")
poem = st.read()
# print(poem)
st.close()

if(word in poem):
    print("Word is present in poem")
else:
    print("Word is not present in poem")