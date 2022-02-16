'''
Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''

li = ["abc", "xyz", "aba", "1221", "1331"]
count = 0
print(li)

for i in range(len(li)):
    st = li[i]
    if len(st) > 2 and st[::1] == st[::-1]:
        count = count + 1
    
print(count)
