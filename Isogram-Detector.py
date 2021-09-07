"""
An Isogram is a word that has no repeating letters, whether they are consecutive or non-consecutive. 

Tells if a Word is an Isogram or Not
"""


# Taking only first word if String has more than one word
s = input().split(' ')[0]

# Printing if it is an Isogram or Not
print(f'You Entered : {s}\nIs \'{s}\' an Isogram ? :', 'Yes' if all(True if s.count(i)==1 else False for i in s) else 'No')