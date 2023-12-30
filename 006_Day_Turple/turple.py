# Create an empty tuple
empty_tuple = ()

# Tuple containing names of siblings
brothers = ('John', 'James', 'Michael')  # Imaginary names
sisters = ('Emily', 'Emma', 'Grace')  # Imaginary names

# Join brothers and sisters tuples
siblings = brothers + sisters

# Count the number of siblings
number_of_siblings = len(siblings)

# Modify the siblings tuple and add parents' names
father = 'George'  # Your father's name
mother = 'Sophia'  # Your mother's name
family_members = siblings + (father, mother)
# Execercise 2
# Unpack siblings and parents from family_members
siblings, father, mother = family_members[:-2], family_members[-2], family_members[-1]

# Create tuples for fruits, vegetables, and animal products
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('meat', 'milk', 'eggs')

# Join the three tuples
food_stuff_tp = fruits + vegetables + animal_products

# Change food_stuff_tp to a list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items
middle_index = len(food_stuff_tp) // 2
middle_items = food_stuff_tp[middle_index] if len(food_stuff_tp) % 2 != 0 else food_stuff_tp[middle_index - 1:middle_index + 1]

# Slice out the first three and last three items
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# Delete food_stuff_tp tuple
del food_stuff_tp

# Check if an item exists in the list
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
estonia_is_nordic = 'Estonia' in nordic_countries
iceland_is_nordic = 'Iceland' in nordic_countries
print(nordic_countries)