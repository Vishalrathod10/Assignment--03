"""Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321" """


# method - 01
def reverse1():
    string = "1234abcd"
    print("sample_string = ",string)
    print('output = ',(string[::-1]))

reverse1()


# method - 02
def reverse2():
  given_string = input('sample string = ')
  print("sample_string = ",given_string)
  print('output = ',(given_string[::-1]))

reverse2()

