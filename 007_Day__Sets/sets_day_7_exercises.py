# Day 7: 30 days of python programming

# # sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print('Length of it_companies set: ', len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)   # Twitter has been added
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Samsung','Huawei','Nokia','LG'])
print(it_companies)
# Remove one of the companies from the set it_companies
it_companies.remove('Huawei')
# What is the difference between remove and discard ?
# Both remove an element from a set but while remove raises a key error if the element is not found in the set, discard does nothing.

# Level 2

# Join A and B
print('Joining A and B: ', A.union(B))  # returns a new set, update will affect the subsequent questions

# Find A intersection B
print('Intersection of A and B: ', A.intersection(B))

# Is A subset of B
print('A is a subset of B : ', A.issubset(B)) # True
# Are A and B disjoint sets
print('A and B are disjoint: ', A.isdisjoint(B))
# Join A with B and B with A: same thing
print('A with B: ', A.union(B))
print('B with A: ', B.union(A))
# What is the symmetric difference between A and B
print('Symmetric difference of A and B: ',A.symmetric_difference(B))  #{27,28}
# Delete the sets completely
del A
del B
print(B) # Raises NameError

# Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print('age_set is smaller than age(the list): ', len(age_st) < len(age))  #definitely from the theory
# Explain the difference between the following data types: string, list, tuple and set
# strings are character types enclosed by quotation marks. They are iterable, ordered and unmutable.
# list is a collection of similar of different data types. They are iterable ,ordered and mutable
# tuples are like lists but are unmutable
# sets contain unique elements in the collection. They are unordered but mutable. 

# I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
print('Unique words in the sentence: ',set(sentence.split()))
print('The number of unique words in the sentence:' , len(set(sentence.split())))
