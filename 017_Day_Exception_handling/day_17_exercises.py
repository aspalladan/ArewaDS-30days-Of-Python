# Day 17: 30 days of Python programming
''' Topics covered
Exception handling
Packing and unpacking in Python
Spreading
Enumerate
Zip
'''


'''
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
Unpack the first five countries and store them in a variable nordic_countries, 
store Estonia and Russia in es, and ru respectively.'''

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries,es,ru = names
print(f'The Nordic countries include: {nordic_countries} ')
print(f'es: {es}, ru: {ru}')