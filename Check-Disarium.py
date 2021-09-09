"""
A number is said to be the Disarium number when the sum of its digit raised to the power of their respective positions is equal to the number itself.

For example, 175 is a Disarium number as follows

1^1 + 7^2 + 5^3 = 1 + 49 + 125 = 175
"""

# Gives A List Of Disariums up till the Number You Entered

try:
    range_ = int(input())
except:
    print('You Didn\'t Entered a Number.\nTaking Input as : 1000')
    range_ = 1000
for num in range(range_+1):
    if num == sum(map(int(i)**(x+1) for i, x in enumerate(str(num)))):
        print(f'{num} is Disarium.')