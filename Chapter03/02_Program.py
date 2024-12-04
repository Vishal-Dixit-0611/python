# Write a python program to fill in a letter template given below with name and date.

letter = '''
Dear <|Name|>,
\tYou are Selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "Vishal").replace("<|Date|>", "5/12/2025"))