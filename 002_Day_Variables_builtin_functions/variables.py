# Day 2: 30 Days of Python Programming
#Excersice 1
# Declare first name variable and assign a value
first_name = 'Abubakar '

# Declare last name variable and assign a value
last_name = 'Suleiman'

# Declare full name variable and assign a value
full_name = first_name + ' ' + last_name

# Declare country variable and assign a value
country = 'Nigeria'

# Declare city variable and assign a value
city = 'Zaria'

# Declare age variable and assign a value
age = 30

# Declare year variable and assign a value
year = 2023

# Declare is_married variable and assign a value
is_married = "No"

# Declare is_true variable and assign a value
is_true = False

# Declare is_light_on variable and assign a value
is_light_on = True

# Declare multiple variables on one line
python, variable, declaration, example = 'Python', 'variables', 'declaration', 'example'

# Return the Python code
print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(age)
print(year)
print(is_married)
print(is_true)
print(is_light_on)
print(python, variable, declaration, example)


#excercise 2
# Check the data type of all variables
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(python))
print(type(variable))
print(type(declaration))
print(type(example))

# Find the length of the first name
length_first_name = len(first_name)
print("Length of first name:", length_first_name)

# Compare the length of the first name and last name
if length_first_name > len(last_name):
    print("First name is longer than last name")
elif length_first_name < len(last_name):
    print("Last name is longer than first name")
else:
    print("First name and last name have the same length")

# Declare num_one and num_two
num_one = 5
num_two = 4

# Perform arithmetic operations
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# Calculate area and circumference of a circle
radius = 30
area_of_circle = 3.14159 * radius ** 2
circum_of_circle = 2 * 3.14159 * radius

# User input for first name, last name, country, and age
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

# Printing the entered values
print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)
