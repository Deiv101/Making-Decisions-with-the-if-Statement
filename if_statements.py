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

for item in range(1, 6):
    list1.append(item)

print(list1)
###########################################################################################################################
list2 = [item for item in range(1, 6)]
list2

###########################################################################################################################
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Conditionals
if a > b:
    print(f"{a} is bigger than {b}.")
    
elif b > a:
    print(f"{b}, the second number, is bigger than {a}, the first number.")
    
elif a > c:
    print(f"{a} is bigger than {c}, the thrid number.")

elif b > c:
    print(f"{b}, the second number, is bigger than {c}, the thrid number.")
    
elif c > a:
    print(f"{c} is bigger than {a}, the first number.")

elif c > b:
    print(f"{c}, the 3rd number, is bigger than {b}, the 2nd number.")

else:
    print(f"The number enter is either bigger or smaller.")

###########################################################################################################################