'''
Write a Python program to sum all the items in a list.
'''

li = [10,20,30,20,10,4.5]
total = 0

for i in range(len(li)):
    total = total + li[i]

print(total)
