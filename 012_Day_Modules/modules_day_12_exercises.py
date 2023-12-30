# Day 12: 30 days of python programming
# Practising importing a function from a module (script) I created myself
from prime_functions import is_prime as prime,all_primes_upto as all_primes

print(prime(5))
print(all_primes(100))



# # Write a function which generates a six digit/character random_user_id.
#   print(random_user_id());

import random
import string
def random_user_id():
    return "".join(str(random.choice(string.ascii_letters + string.digits)) for i in range(6))

print(random_user_id())

#   '1ee33d'
# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf

# Testing this for my function
["".join(str(random.choice(string.ascii_letters + string.digits)) for i in range(6)) for j in range(6)]



def random_user_id_gen_by_user():
    a = int(input("Enter the number of characters: "))
    b = int(input("Enter the number of IDs: "))
    return ["".join(str(random.choice(string.ascii_letters + string.digits)) for i in range(a)) for j in range(b)]

# unpack operator in print function    #learning bonus
s =["".join(str(random.choice(string.ascii_letters + string.digits)) for i in range(6)) for j in range(6)]
print(*s,sep='\n')



# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form

def rgb_color_gen():
    a = ','.join(str(random.randint(0,255)) for i in range(3))
    return 'rgb('+ a + ')'
print(rgb_color_gen())



# Exercises: Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
# There's no task 6

def list_of_hexa_colors(x):
     a= ["".join(str(random.choice('abcdef' + string.digits)) for i in range(6)) for j in range(x)]
     b =['#' + item for item in a]
     return b
list_of_hexa_colors(6)
# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def list_of_rgb_colors(x):
    return [rgb_color_gen() for i in range(x)]

list_of_rgb_colors(7)

string.digits

# Write a function generate_colors which can generate any number of hexa or rgb colors.

def generate_colors(fun,x):
    if fun == 'hexa':
        result = list_of_hexa_colors(x)
    elif fun == 'rgb':
        result = list_of_rgb_colors(x)

    return result

generate_colors('hexa',3)
generate_colors('rgb',1)

#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']




# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list(list):
    random.shuffle(list)
    return list
print(shuffle_list([1,2,3,4,5]))
    
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_nums():
    return random.sample([0,1,2,3,4,5,6,7,8,9],k=7)
print(unique_random_nums())