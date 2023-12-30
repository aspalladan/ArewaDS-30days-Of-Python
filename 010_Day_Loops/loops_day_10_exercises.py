# Day 10: 30 days of python programming
# Loops

## Exercise level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(11):
    print(number)

number = -1
while number < 10:
    number +=1
    print(number)
# Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10,-1,-1):
    print(i)


x = 11
while x > 0:
    x -= 1
    print(x)

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######


for i in range(8):
    print('#' * i)



# Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for i in range(9):
    print('#  ' * 8)


# Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for i in range(11):
    print(f'{i} x {i} =  {i * i}')
#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in list:
    print(item)
# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i%2 == 0:
        print(i)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i%2==1:
        print(i)


## Exercise level 2

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
a = 0
for i in range(101):
    a += i
print(f'The sum of all numbers is {a}')
# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# initiate the container for the sums, a for even, b for odds
a = 0
b = 0
for i in range(101):
    if i%2 ==0:
        a += i
    else:
        b+=i
print(f'The sum of all evens is {a} and the sum of all odds is {b}')

# Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries containing the word land.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

for country in countries:
    if 'land' in country:
        print(country)

# Finland
# Iceland
# Ireland
# Marshall Islands
# Netherlands
# New Zealand
# Poland
# Solomon Islands
# Swaziland
# Switzerland
# Thailand
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_list = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(fruit_list)-1,-1,-1):
    print(fruit_list[i])

# Go to the data folder and use the countries_data.py file.
# importing the countries_data list from the country_data.py file
from country_data import countries_data


# What are the total number of languages in the data
language_count = 0
for i in range(len(countries_data)):
    language_count += len(countries_data[i]['languages'])
print(language_count)
# There are 368 languages(not accounting for duplicates)



# Find the ten most spoken languages from the data


# for most spoken languages, get a list of all languages and move from there.
# I understood most spoken from the perspective of the number of countries a language is spoken in
languages = []
for i in range(len(countries_data)):
    languages.extend(countries_data[i]['languages'])
print(languages)

#arranging the languages
# using the list of languages to get the language count
print('Count of languages: ',len(languages))

# Accounting for duplicates
print('Count of unique languages: ',len(set(languages)))  # 112

languages.sort()

# looping to get dict of languages
lang = {}
for language in languages:
    if language in lang:
        lang[language] += 1
    else:
        lang[language] = 1
print(lang)
# sorting the list of the tuples to get the most spoken languages
sorted_lang = sorted(lang.items(), key= lambda x:x[1],reverse=True)
sorted_lang # contains the languages arranged based on values
# for the top ten, loop 

for i in range(10):
    print(sorted_lang[i])
# option 2 for top ten : slicing the list, same answer
sorted_lang[:10]

# ('English', 91)
# ('French', 45)
# ('Arabic', 25)
# ('Spanish', 24)
# ('Portuguese', 9)
# ('Russian', 9)
# ('Dutch', 8)
# ('German', 7)
# ('Chinese', 5)
# ('Italian', 4)


# Find the 10 most populated countries in the world
population = {}
for i in range(len(countries_data)):
    keys = countries_data[i]['name']
    values = countries_data[i]['population']
    population[keys] = values
print(f"Countries populations: {population}")

# sorting the list of the tuples to get the most spoken languages
sorted_pop = sorted(population.items(), key= lambda x:x[1],reverse=True)
 # contains the languages arranged based on values
# for the top ten, another loop
for i in range(10):
    print(sorted_pop[i])
# or slicing list
sorted_pop[:10]
print(f"most populated countries in the world with their populations: {sorted_pop[:10]} ")
