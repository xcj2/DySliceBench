# coding: utf-8
# Your code here!

def reverse(s, i, j):
    tmp = ''
    for i in range(j, i-1, -1):
        tmp += s[i]
    return s[:i] + tmp + s[j+1:]

def pprint(s, i, j):
    print(s[i:j+1])

def replace(s, i, j, r):
    tmp = s[:i] + r + s[j+1:]
    return tmp

word = input()
# word = 'abcde'
loop = int(input())
# loop = 3
# arr = [
#     'replace 1 3 xyz',
#     'reverse 0 2',
#     'print 1 4',
#     ]

for i in range(loop):
    line = input().split()
    # line = arr[i].split()
    # print(word)
    if line[0] == 'replace':
        word = replace(word, int(line[1]), int(line[2]),line[3])
    elif line[0] == 'reverse':
        word = reverse(word, int(line[1]), int(line[2]))
    elif line[0] == 'print':
        pprint(word, int(line[1]), int(line[2]))
    
    
    

