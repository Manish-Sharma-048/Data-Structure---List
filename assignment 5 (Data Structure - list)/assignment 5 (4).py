'''
Write a Python program to remove duplicates from a list.
'''

li = [10,20,30,20,10,30,20,10,40]
li2 = []

for i in range(len(li)):
    if li[i] not in li2:
        li2.append(li[i])

print(li2)
