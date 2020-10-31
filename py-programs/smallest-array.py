#smallest element in an array
size = int(input('Enter the size of an array : '))
arr = []

for i in range(size):
  element = int(input())
  arr.append(element)
print('The smallest element is ', min(arr))