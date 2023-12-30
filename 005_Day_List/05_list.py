# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
more_than_five = [1, 'two', True, 3.14, 'five']

# Find the length of your list
length_of_list = len(more_than_five)

# Get the first, middle, and last items of the list
first_item = more_than_five[0]
middle_item = more_than_five[length_of_list // 2]  # Using floor division to get the middle
last_item = more_than_five[-1]

# Declare a list with mixed data types
mixed_data_types = ['John', 30, 180, 'Single', '123 Main St']

# Declare a list of IT companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list and number of companies
print(it_companies)
print(len(it_companies))

# Print the first, middle, and last company
print(it_companies[0])
print(it_companies[length_of_list // 2])
print(it_companies[-1])

# Modify one of the companies
it_companies[1] = 'Twitter'

# Add an IT company
it_companies.append('LinkedIn')

# Insert an IT company in the middle
it_companies.insert(len(it_companies) // 2, 'Salesforce')

# Change a company name to uppercase (excluding IBM)
it_companies[4] = it_companies[4].upper()

# Join the it_companies with a string '#; '
joined_companies = '#; '.join(it_companies)

# Check if a certain company exists
print('Microsoft' in it_companies)

# Sort the list
it_companies.sort()

# Reverse the list
it_companies.reverse()

# Slicing
first_three = it_companies[:3]
last_three = it_companies[-3:]
middle_companies = it_companies[3:-3]

# Remove first, middle, and last IT companies
it_companies.pop(0)
it_companies.pop(len(it_companies) // 2)
it_companies.pop()

# Remove all IT companies
it_companies.clear()

# Destroy the list
del it_companies

# Join front_end and back_end lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end

# Insert Python and SQL after Redux in full_stack
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Redux') + 2, 'SQL')

# Exercise 2
# List of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)

# Add min and max ages again to the list
ages.extend([min_age, max_age])

# Find the median age
sorted_ages = sorted(ages)
middle = len(sorted_ages) // 2
median_age = (sorted_ages[middle] + sorted_ages[~middle]) / 2  # ~middle gives the other middle index if two

# Find the average age
average_age = sum(ages) / len(ages)

# Find the range of ages
age_range = max(ages) - min(ages)

# Compare (min - average) and (max - average)
comparison = abs(min_age - average_age) > abs(max_age - average_age)

# List of countries
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# Find the middle country or countries
middle_index = len(countries) // 2
middle_countries = [countries[middle_index]] if len(countries) % 2 != 0 else countries[middle_index - 1:middle_index + 1]

# Divide the countries list into two equal or nearly equal lists
half_length = len(countries) // 2
first_half = countries[:half_length] if len(countries) % 2 == 0 else countries[:half_length + 1]
second_half = countries[half_length:]

# Unpack the first three countries and the rest as scandic countries
first_three, *scandic_countries = countries[:3], countries[3:]
