import sys

M = 1046527
def h1(key):
    return key % M

def h2(key):
    return 1 + (key %(M-1))

def h3(key, i):
    return (h1(key) + i*h2(key)) % M

word_dic = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
def getkey(text):
    sum = 0
    p = 1
    for c in text:
        sum += p*word_dic[c]
        p *= 5
    return sum

dict = [None for i in range(M)]
def find(text):
    key = getkey(text)
    i = 0
    while i < M:
        h = h3(key, i)
        if dict[h] == None:
            break
        elif dict[h] == text:
            return True
        i += 1
    return False

def insert(text):

    key = getkey(text)
    i = 0
    while i < M:
        j = h3(key, i)
        if dict[j] == None:
            dict[j] = text
            break
        else:
            i += 1

n = int(input())
operations = sys.stdin.readlines()
for ope in operations:
    op, text = ope.rstrip().split(' ')
    if op == 'insert':
        insert(text)
    elif op == 'find':
        rst = find(text)
        if rst:
            print('yes')
        else:
            print('no')

