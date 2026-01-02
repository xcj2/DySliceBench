import sys

M = 1044697
H = [None] * M

table = str.maketrans({"A":"1","C":"2","G":"3","T":"4"})


def getChar(ch):
    if ch == "A":
        return 1
    elif ch == "C":
        return 2
    elif ch == "G":
        return 3
    elif ch == "T":
        return 4
    else:
        return 0

def getKey(string):
    sum = 0
    p = 1
    for i in range(len(string)):
        sum += p*(getChar(string[i]))
        p *= 5
    return sum

#print(getKey(string))

def h1(key):
    return key % M

def h2(key):
    return 1 + (key % (M-1))

# 関数の中のwhile文はreturnで抜け出せる
def find(string):
    i = 0
    key = getKey(string)
    while True:
        h = (h1(key) + i * h2(key)) % M
        if H[h] == string:
            return 1
        elif H[h] is None:
            return 0
        else:
            i += 1

def insert(string):
    i = 0
    key = getKey(string)
    while True:
        h = (h1(key) + i * h2(key)) % M
        if H[h] is None:
            H[h] = string
            break
        else:
            i += 1


input = sys.stdin.readline
n = int(input())

for _ in range(n):
    com,string = input().split()
    if com == "insert":
        insert(string)
    elif com == "find":
        if find(string):
            print("yes")
        else:
            print("no")
