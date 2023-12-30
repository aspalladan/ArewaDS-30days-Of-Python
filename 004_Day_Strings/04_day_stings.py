
# Concatenate strings
concatenated_string1 = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
concatenated_string2 = ' '.join(['Coding', 'For', 'All'])

# Declare and print a variable
company = "Coding For All"
print(company)

# Print length of the string
print(len(company))

# Convert to upper and lower case
print(company.upper())
print(company.lower())

# Formatting the string
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut out the first word
first_word = company.split()[0]

# Check for word existence
print('Coding' in company)

# Replace a word in a string
print(company.replace('Coding', 'Python'))

# Split strings
print(company.split())
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

# Indexing
print(company[0])
print(company[-1])
print(company[10])

# Acronyms
acronym1 = ''.join(word[0] for word in "Python For Everyone".split())
acronym2 = ''.join(word[0] for word in "Coding For All".split())
print(acronym1)
print(acronym2)

# Finding index positions
print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))

# Finding occurrences in sentences
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.rindex('because'))
print(sentence[sentence.find('because'):sentence.rfind('because')+len('because')])

# Checking substrings
print(company.startswith('Coding'))
print(company.endswith('coding'))

# Stripping spaces
string_with_spaces = '   Coding For All      '
print(string_with_spaces.strip())

# isidentifier() method
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# Joining strings
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)
print(joined_libraries)

# Escape sequences
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# String formatting
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Mathematical operations
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")
