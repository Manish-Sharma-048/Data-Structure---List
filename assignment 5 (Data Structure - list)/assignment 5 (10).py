'''
Write a Python program to get unique values from a list.
'''

l = [10,20,30,60,50,40,30,20,10]
li = []

for i in l:
    if i not in li:
        li.append(i)

print("The unique values in the list are: ",li)
