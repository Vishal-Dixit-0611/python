# Write a python function to remove a given word from a list and strip it at the same time.

def rem(l, word ):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Education", "Presentation", "Transportation", "Function","ta"]

print(rem(l, "tion"))
