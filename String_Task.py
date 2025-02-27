def remove_vowels(char):
    return char not in vowel 

vowel="aeiouyAEIOUY"

string = input()

new_string = '.'.join(filter(remove_vowels, string))

print(f".{new_string.lower()}")