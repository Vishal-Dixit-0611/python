# Write a Program to create a dictionary of Hindi words with values as their English translation. 
# Provide User with an option to look it up!

dist = {
    "Parda": "Curtain",
    "Kursi": "Chair",
    "Pani": "Water",
    "Hwa": "Air",
    "Aag": "Fire"
}

item = input("Enter the item you want to search: ")
print(dist[item])
