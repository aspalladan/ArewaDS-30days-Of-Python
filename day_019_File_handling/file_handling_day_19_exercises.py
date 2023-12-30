# Day 19: 30 days of python programming

# importing required libraries
import re, json, csv


'''Write a function which count number of lines and number of words in a text.
All the files are in the data folder: a) Read obama_speech.txt file and count number of lines and words 
b) Read michelle_obama_speech.txt file and count number of lines and words 
c) Read donald_speech.txt file and count number of lines and words 
d) Read melania_trump_speech.txt file and count number of lines and words'''

def count_words_lines(file):
    with open(file) as f:
        lines = f.readlines()
        words = []
        for line in lines:
            # removing all characters that are not whitespace or alphanumeric using regex
            line = re.sub(r'[^\w\s]','',line)
            words.extend(line.split())
    print(f'The number of lines and words in the file are {len(lines)} and {len(words)} respectively')
count_words_lines('day_019/melania_trump_speech.txt')
count_words_lines('day_019/donald_speech.txt')
count_words_lines('day_019/michelle_obama_speech.txt')
count_words_lines('day_019/obama_speech.txt')



# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

'''Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 10))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic'),
(24, 'Spanish'),
(9, 'Russian'),
(9, 'Portuguese'),
(8, 'Dutch'),
(7, 'German'),
(5, 'Chinese'),
(4, 'Swahili'),
(4, 'Serbian')]'''

'''Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 3))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic')]'''

def most_spoken_languages(file,n):
    '''
    Takes a filepath and an integer,n as arguments and returns the n most spoken languages in the world
    '''
    with open(file) as f:
        list = json.loads(f.read())
    # looping to get dict of languages
    languages = []
    for i in range(len(list)):
        languages.extend(list[i]['languages'])
    lang = {}
    for language in languages:
        lang[language] = lang.get(language,0) + 1
    # sorting the list of the tuples to get the most spoken languages
    sorted_lang = sorted(lang.items(), key= lambda x:x[1],reverse=True) # contains the languages arranged based on values
    result = [(item[1],item[0]) for item in sorted_lang]
    return result[:n]
most_spoken_languages('day_019/countries_data.json',10)


# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

'''Your output should look like this
print(most_populated_countries(filename='./data/countries_data.json', 10))

[
 {'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000},
{'country': 'Indonesia', 'population': 258705000},
{'country': 'Brazil', 'population': 206135893},
{'country': 'Pakistan', 'population': 194125062},
{'country': 'Nigeria', 'population': 186988000},
{'country': 'Bangladesh', 'population': 161006790},
{'country': 'Russian Federation', 'population': 146599183},
{'country': 'Japan', 'population': 126960000}
 ]'''

'''Your output should look like this

print(most_populated_countries(filename='./data/countries_data.json', 3))
 [
{'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000}
]'''


def most_populated_countries(filename,n):
    '''
    Takes a file path and an integer,n as arguments and returns the n most populated countries in the world
    '''
    with open(filename) as f:
        dic_list = json.loads(f.read())
    population = dict()
    for i in range(len(dic_list)):
        keys = dic_list[i]['name']
        values = dic_list[i]['population']
        population[keys] = values
    # sorting by values of the population, descending (list of tuples)
    sorted_lt = sorted(population.items(), key= lambda x:x[1],reverse=True)
    final_list = [{'country':item[0],'population':item[1]} for item in sorted_lt]
    return final_list[:n]

most_populated_countries('day_019/countries_data.json',7)




# Exercises: Level 2
# Extract all incoming email addresses as a list from the email_exchange_big.txt file.

with open('day_019/email_exhange_big.txt') as f:
    lines = f.readlines()
email_addresses = []
for line in lines:
    #using regex to get alphanumeric characters before and after and @ symbol. \S is non-whitespace characters
    email_addresses.extend(re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line))
email_addresses[:]  # worked: contains all email addresses as a list. 



''' Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
    # Your output should look like this
    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
     (6, 'of'),
    (5, 'and'),
    (4, 'a'),
     (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # Your output should look like this
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]'''

def find_most_common_words(file,n=10):
    '''
    Returns a list of tuples showing the count of the n most common words in the document, file
    '''
    with open(file) as f:
        lines = f.readlines()
    words = []
    for line in lines:
        # removing all characters that are not whitespace or alphanumeric using regex, don't want punctuation affecting count
        line = re.sub(r'[^\w\s]','',line)
        words.extend(line.split())
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word,0) + 1
    words_sorted = sorted(words_dict.items(),key=lambda x:x[1],reverse=True)
    result = [(word[1],word[0]) for word in words_sorted]
    return result[:n]

find_most_common_words('day_019/donald_speech.txt',5)
# function is up and running.

# Use the function, find_most_frequent_words to find: 
# a) The ten most frequent words used in Obama's speech
print(find_most_common_words('day_019/obama_speech.txt')) 
# b) The ten most frequent words used in Michelle's speech 
print(find_most_common_words('day_019/michelle_obama_speech.txt'))
# c) The ten most frequent words used in Trump's speech 
print(find_most_common_words('day_019/donald_speech.txt'))
# d) The ten most frequent words used in Melina's speech
print(find_most_common_words('day_019/melania_trump_speech.txt'))



'''Write a python application that checks similarity between two texts. 
It takes a file or a string as a parameter and it will evaluate the similarity of the two texts.
For instance check the similarity between the transcripts of Michelle's and Melina's speech. 
You may need a couple of functions, function to clean the text(clean_text), 
function to remove stop words(remove_stop_words) and finally to check the similarity(check_text_similarity). 
List of stop words are in the data directory
# 179 stops words '''
def clean_text(file):
    '''
    Returns all the words in a text after removing the punctuations and others
    '''
    with open(file) as f:
        lines = f.readlines()
        words = []
        for line in lines:
            # removing all characters that are not whitespace or alphanumeric using regex
            line = re.sub(r'[^\w\s]','',line)
            words.extend(line.split())
    return words


clean_text('day_019/michelle_obama_speech.txt') # worked

# onto removing stop words
# importing stop_words list from stop_words.py
from stop_words import stop_words
def remove_stop_words(list):
    '''Removes stop words, i.e. commonly used words that search engines are programmed to ignore, from a list of words'''
    return [word for word in list if word.lower() not in stop_words]
remove_stop_words(clean_text('day_019/michelle_obama_speech.txt'))  # handled

# next, function for similarity
def check_text_similarity(list_one,list_two):
    '''Gives a percentage of similar words in two different lists'''
    res = [x for x in (list_one + list_two) if x in list_one and x in list_two]
    similar_words_percent = (len(res)/(len(list_one) + len(list_two))) * 100
    return similar_words_percent
check_text_similarity(['apple','banana','mango','pawpaw'],['apple','mango','pear']) # worked.


# combining the functions 
def comparing_text_in_file_similarity(file_one,file_two):
    '''Gives the percentage of similar words in two different files'''
    file_one_words = remove_stop_words(clean_text(file_one))
    file_two_words = remove_stop_words(clean_text(file_two))
    return check_text_similarity(file_one_words,file_two_words)

comparing_text_in_file_similarity('day_019/michelle_obama_speech.txt','day_019/melania_trump_speech.txt') # Got 41.73% similarity. 
# Find the 10 most repeated words in the romeo_and_juliet.txt
# most common and most repeated are the same

print(find_most_common_words('day_019/romeo_and_juliet.txt'))


'''Read the hacker news csv file and find out:
a) Count the number of lines containing python or Python 
b) Count the number lines containing JavaScript, javascript or Javascript
c) Count the number lines containing Java and not JavaScript'''

with open('day_019/hacker_news.csv',newline='') as f:
    csv_reader = csv.reader(f,delimiter=',')
    python_rows = 0
    javascript_rows = 0
    java_rows = 0
    for row in csv_reader:
        for i in range(len(row)):
            if re.findall(r'[Pp]ython',row[i]):
                python_rows += 1
            elif re.findall(r'[Jj]ava[Ss]cript',row[i]):
                javascript_rows +=1
            elif re.findall(r'Java$',row[i]):
                java_rows +=1
print(f'the number of lines containing a,b and c respectively are: {python_rows}, {javascript_rows} and {java_rows}')

