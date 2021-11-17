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