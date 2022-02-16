'''
Write a Python program to print the numbers of a specified list after removing even numbers from it.
'''

l = [1,21,32,43,35,6,71]

li = [l[i] for i in range(len(l)) if(l[i]%2!=0)]
print("Entered list: ",l)
print("Updated list: ", li)
