""" Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20 """

# method -01 
def sum():
  num = int(input('please enter number of elements in list = '))
  lis1 = []
  for i in range(1,num+1):
    sample_list = int(input('elements in list to be added = '))
    lis1.append(sample_list)
  print('given list = ',lis1)
  addition = 0

  for i in lis1:
    print(i)
    addition += i
  print('summation for given numbers in list = ',addition)

sum()


# method -02
def sum():
  lis2 = [8, 2, 3, 0, 7]
  print('given list = ',lis2)
  addition = 0

  for i in lis2:
    print(i)
    addition += i
  print('summation for given numbers in list = ',addition)

sum()