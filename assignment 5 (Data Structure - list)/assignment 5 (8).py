'''
Write a Python program to convert a list of characters into a string.
'''

l = ["hi", "hello", "hey"]

string = ""

for i in range(3):
    string = string + l[i] + " "

print(string)
print(type(string))
