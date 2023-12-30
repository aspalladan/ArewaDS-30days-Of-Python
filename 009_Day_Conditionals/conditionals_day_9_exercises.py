 # Day 9: 30 days of python programming

# Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:

# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

a = int(input('Enter your age: '))
if a >= 18:
    print('You are old enough to drive')
else:
    print(f'You need {18-a} more years to learn to drive')


# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 
# 'years' for bigger differences, and a custom text if my_age = your_age. Output:

# Enter your age: 30
# You are 5 years older than me.


my_age = 28
your_age = int(input('Enter your age:'))


if my_age > your_age:
    if my_age - 1 == your_age:
        print("I am one year older than you")
    else:
        print(f'I am {my_age - your_age} years older than you')
elif my_age < your_age:
    if my_age + 1 == your_age:
        print('You are one year older than me')
    else:
        print(f'You are {your_age - my_age} years older than me')
else:
    print('We are the same age')


# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, 
# else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

a = int(input('Enter number one:'))
b = int(input('Enter number two:'))
if a < b:
    print('a is smaller than b')
elif a > b:
    print('a is greater than b')
else:
    print('a is equal to b')


# Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

score = 60

if score <=100 and  score >= 90:
    print("A")
elif score <= 89 and score >= 70:
    print("B")
elif score <=69 and score >= 60:
    print("C")
elif score <= 59 and  score >= 50:
    print("D")
else:
    print("F")



# Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer

user_input = 'December'
if user_input == 'September' or user_input == 'October' or user_input == 'November':
    print("The season is Autumn")
elif user_input == 'December' or user_input == 'January' or user_input == 'February':
    print('The season is Winter')
elif user_input == 'March' or user_input == 'April' or user_input == 'May':
    print('The season is Spring')
else:
    print('The season is Summer')


# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruit = 'cashew'
if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else: 
    print('The fruit already exists in the list')



# Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }


# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    print(person['skills'][int(len(person['skills'])/2)])
# Check if the person dictionary has skills key, 
# if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print(person['skills'])
# If a person skills has only JavaScript and React, 
# print('He is a front end developer'),
#  if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
#  if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in person:
    if 'Node' and 'MongoDB' in person['skills']:
        if 'React' in person['skills']:
            print('He is a fullstack developer')
        elif 'Python' in person['skills']:
            print('He is a backend developer')
    elif 'JavaScript' and 'React' in person['skills']:
        print('He is a frondend developer')
    else: 
        print('Unknown title')
             


# If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
first_name = person['first_name']
last_name = person['last_name']
country = person['country']

if person['is_married']==True and person['country']=='Finland':
    print(f'{first_name} {last_name} lives in {country}. He is married.')