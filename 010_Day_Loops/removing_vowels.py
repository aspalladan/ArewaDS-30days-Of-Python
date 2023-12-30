# Programme to remove vowels from strings in a file 
string = input('Write your sentence: ')
vowels = ['a','e','i','o','u','A','E','I','O','U']
stripped = ''
for i in range(len(string)):
    if string[i] not in vowels:
        stripped += string[i]
print(stripped)

    
