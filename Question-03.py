"""Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 1 """


def alphabets():
  given_string1 = input('sample string = ')
  print("sample_sting = ",given_string1)
  count_upper = 0
  count_lower = 0

  for i in given_string1:
    if i.isupper():
      count_upper += 1
    elif i.islower():
      count_lower +=1
  print('upper letters = ',count_upper)
  print('lower letters = ',count_lower)

alphabets()