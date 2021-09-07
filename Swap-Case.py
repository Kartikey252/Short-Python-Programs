"""
Swap Case of a String in python
"""


s = input()

# Using Python's Function swapcase()
print(f'Case Swapped String by using swapcase() Function : {s.swapcase()}')

# Using my Method
swappedString = ''.join(i.upper() if ord(i)>96 else i.lower() for i in s)
print(f'Case Swapped String by my method : {swappedString}')