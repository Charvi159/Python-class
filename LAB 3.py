#1
'''a = input("Enter a string of your choice: ")
x=a.count('a')+a.count('A')+a.count('e')+a.count('E')+a.count('i')+a.count('I')+a.count('o')+a.count('O')+a.count('u')+a.count('U')
print("The number of vowels in the string is", x)'''

#2
def to_lowercase(s):
    lower_string = ""
    for char in s:
        if 'A' <= char <= 'Z':  # Check if the character is uppercase
            lower_string += chr(ord(char) + 32)
        else:
            lower_string += char
    return lower_string

# Example usage
print(to_lowercase("Hello World!"))  # Output: "hello world!"

def to_uppercase(s):
    upper_string = ""
    for char in s:
        if 'a' <= char <= 'z':  # Check if the character is lowercase
            upper_string += chr(ord(char) - 32)
        else:
            upper_string += char
    return upper_string

# Example usage
print(to_uppercase("Hello World!"))

def toggle_case(s):
    toggle_string = ""
    for char in s:
        if 'A' <= char <= 'Z':  # Check if the character is uppercase
            toggle_string += chr(ord(char) + 32)
        elif 'a' <= char <= 'z':  # Check if the character is lowercase
            toggle_string += chr(ord(char) - 32)
        else:
            toggle_string += char
    return toggle_string

#3
'''string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string1 in string2:
    print('present')
else:
    print('not present')'''


#4
'''string1 = input("Enter parent string: ")
string2 = input("Enter string to remove: ")
string1=string1.replace(string2,'')
print(string1)'''
