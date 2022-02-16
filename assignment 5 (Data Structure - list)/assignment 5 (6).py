'''
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''

li = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
t = [0,4,5]

t.sort(reverse = True)

for i in t:
    val = li[i]
    li.remove(val)

print(li)
