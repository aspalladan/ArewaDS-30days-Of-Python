# Day 18: 30 days of Python programming
# Exercises: Day 18
# importing the re module for regular expressions
import re

# Exercises: Level 1

# What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = paragraph.replace('.','').split(' ')
dict = {}
for word in words:
    dict[word] = dict.get(word,0) + 1
sort_keysval = sorted(dict.items(),key = lambda x:x[1], reverse=True)
sort_keysval[0] # love occurs 6 times in the paragraph.


'''The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-4) # 12  '''
string = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
regex= r'-\d|\d'
points = re.findall(regex,string)
print(points)   # ['-1', '-1', '-3', '-4', '0', '2', '4', '8']
points.sort()
# Getting the numbers as integers from strings
numbers = [int(i) for i in points]
numbers.sort()  # sorting from highest to lowest
distance = numbers[-1] - numbers[0]
print(f'The distance between the two furthest particles is {distance} ') # got the answers 12

# Exercises: Level 2
'''Write a pattern which identifies if a string is a valid python variable

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True   '''

pattern = r"^[_a-z]\w*$"
def is_valid_variable(name):
    pattern = r"^[_a-z]\w*$"
    if not re.match(pattern,name):
        print(False)
    else:
        print(True)

# Exercises: Level 3

# Clean the following text. After cleaning, count three most frequent words in the string.

# sentence = %I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# print(clean_text(sentence));
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
# print(most_frequent_words(cleaned_text)) ''' 
 # [(3, 'I'), (2, 'teaching'), (2, 'teacher')] 
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
pattern = r'[^\w\s]'
clean_sentence = re.sub(pattern,'',sentence)

def most_frequent_words(text):
    '''This function returns the three most frequent words in clean sentences i.e. sentences without punctuation marks.
    '''
    words = text.split()
    d = {}
    for word in words:
        d[word] = d.get(word,0) + 1
    list = [(val,key) for key,val in d.items()]
    list.sort(reverse=True)
    return list[:3]

most_frequent_words(clean_sentence)
