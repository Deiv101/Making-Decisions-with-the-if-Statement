# fig02_1.py
"""Comparing integers using if statements and comparison operators."""

print('Enter two integers, and I will tell you the relationships they satisfy.')

# read first integer
number1 = int(input('Enter first integer: '))

# read second integer
number2 = int(input('Enter second integer: '))

if number1 == number2:
    print(number1, 'is equal to ', number2)

if number1 != number2:
    print(number1, 'is not equal to', number2)

if number1 < number2:
    print(number1, 'is less than', number2)

if number1 > number2:
    print(number1, 'is greater than', number2)

if number1 >= number2:
    print(number1, 'is greater than or equal to', number2)

if number1 <= number2:
    print(number1, 'is less than or eqaul to', number2)

###########################################################################################################################
print("\n")
# fig02_02.py
"""Find the minimum of three values."""

a = int(input('Enter first integer: '))
b = int(input('Enter second integer: '))
c = int(input('Enter third integer: '))

minimum = a

if b < minimum:
    minimum = b

if c < minimum:
    minimum = c

print('Minimum value is', minimum)

###########################################################################################################################
grade = float(input("Enter pupil's grade: "))

if grade >= 60:
    print('The student has passed.')

if grade <= 60:
    print('The student has failed.')

###########################################################################################################################
print("\n")

grade = 87
result = ('Passed' if grade >= 60 else 'Failed.')

###########################################################################################################################
print("\n")

grade = 77

if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')

###########################################################################################################################
# Nested
color_names = ['red', 'orange', 'yellow', 'green', 'white', 'blue']

for color in color_names:
    if color == 'red':
        print(f'That color is {color}.')
    elif color == 'magenta':
        print(f'{color} is not in the list.')
    else:
        print(f'That color is any other color other than {color}.')

###########################################################################################################################
# Lists comprehension
list1 = []