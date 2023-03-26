n = int (input ("Enter number of elements: "))
list = []
for i in range (n):
    x = int(input())
    list.append(x)
pos=[num for num in list if num>=0]
print('Positve numbers in the list: ',pos)
