#Create a function that reverses a string:
#'Hi My Name is Mich' should be:
# 'hciM si emaN yM iH'
def reverse(str):
  result = ''
  # Run a loop from len(str)-1 to 0 
  #One by one append char from end to start in the new string 
  #(Last Item , Inclusive, Difference between next element and current element)
  for i in range(len(str)-1,-1,-1):
    result = result + str[i]

  print(result)


def reverse2(str):
  reverseChar = reversed(str)
  print(''.join(reverseChar))

reverse('My Name is Mich')
reverse2('My Name is Mich')


