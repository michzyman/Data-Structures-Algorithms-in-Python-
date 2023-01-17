letters = ['a', 'd', 'z', 'e', 'r', 'b']
print(letters)
print(letters.sort())

basket = [2,65,34,2,1,7,8]
basket.sort()
print(basket)

"""
Important .sort() in javacript does not work with unicode characters 
example: if you have an list of words in spanish and want to sort the words (including the words with ' then it will not work)
In python the .sort() function works with Unicode characters 
The sort() method uses the default sorting algorithm which is based on the comparison of the elements, and it can handle sorting of elements of different types, including strings that contain Unicode characters.

When sorting strings that contain Unicode characters, the default behavior is to sort based on the Unicode code point values of each character.

For example, if you have a list of strings containing Unicode characters:
"""