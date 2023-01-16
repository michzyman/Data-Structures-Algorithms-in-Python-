"""
The function takes a string as an input and checks if its length is 0. 
If it is, it returns the empty string. 
If it's not it returns the reverse of the string obtained by removing 
the first character and concatenating the first character to it.

The function calls itself with the substring of the original string, 
starting from the second character and ending at the end of the string. 
It keeps calling itself until the input string is an empty string, at which point 
it concatenates the first character of the original string to the reversed substring 
returned by the previous recursive call.

For example, when the input is "hello", the first call to the function is with the substring "ello",
 and the first character is "h".
The next call is with the substring "llo" and the first character is "e" and so on.
Finally, when the input is an empty string, the function concatenates the first character "o" 
to the reversed substring "lleh" and returns "olleh" which is the reverse of the original string.

"""
def reverseString(string):
    if len(string) == 0:
        return string
    else:
        return reverseString(string[1:]) + string[0]

print(reverseString('hello!'))