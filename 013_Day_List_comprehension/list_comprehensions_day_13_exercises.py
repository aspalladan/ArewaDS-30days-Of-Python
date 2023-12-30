# Day 13: 30 days of Python programming
# Exercises: Day 13

# Filter only negative and zero in the list using list comprehension
numbers = [-4,-3,-2,-1,0,2]
[number for number in numbers if number <=0] # [-4, -3, -2, -1, 0]


# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists = [[[1,2,3]],[[4,5,6]],[[7,8,9]]]
# output = [1,2,3,4,5,6,7,8,9]
# 1. In steps
a = [number for row in list_of_lists for number in row]
b = [number for row in a for number in row]
# Trying at once

# levels = number -> list > row -> list_of_lists
c = [number for row in list_of_lists for list in row for number in list]
print(c)


# Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

tpl_list = [(i**1,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)] 
print(tpl_list)


# Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# tpl -> row -> list
[[tpl[0].upper(),tpl[0][:3].upper(), tpl[1].upper()] for row in countries for tpl in row]

# Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]

[{'country':tpl[0],'city':tpl[1]} for row in countries for tpl in row]

# Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

# output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
[(name[0] + " " + name[1]) for row in names for name in row]

# Write a lambda function which can solve a slope or y-intercept of linear functions.

# y = m * x + c
# chose y-intercept
y_i_c = lambda m,c,x:c  # when x is zero, value of y
y_i_c(2,4,2)


