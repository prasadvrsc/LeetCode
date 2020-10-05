'''
Imagine that we have to find the number of vowels in a given string. 
We know that the English alphabet contains 55 vowels: a, e, i, o, ua,e,i,o,u. 
Let’s solve this problem using both iterative and recursive methods.
'''

#Iterative
def count_vowels(string): 
    count = 0
    for i in range(len(string)):
        if is_char_vowel(string[i]):
            count +=1
    return count

def is_char_vowel(character):
    character = character.lower()
    vowel_string = "aeiou"
    if character in vowel_string:
        return 1
    return 0

#Recursive
def count_vowels_recursive(string):
    return count_vowels_helper(string, len(string))

def count_vowels_helper(string, length):
    #Base Case
    if length == 1:
        return is_char_vowel(string[0])

    return count_vowels_helper(string, length-1) + is_char_vowel(string[length-1])

    

#Test Case
string = "Prasad Vaizurs"
print(count_vowels(string)) 
print(count_vowels_recursive(string)) 


