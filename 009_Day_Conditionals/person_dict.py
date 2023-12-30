person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['React','JavaScript','Python','Node'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    print(person['skills'][len(person['skills'])//2])
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
    if 'React' and 'Node' and 'MongoDB' in person['skills']:
        print('He is a fullstack developer')
    elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
        print('He is a backend developer')
    elif 'JavaScript' and 'React' in person['skills']:
        print('He is a frontend developer')
    else:
        print('Unknown title')
# work in progress
# another attempt
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
             