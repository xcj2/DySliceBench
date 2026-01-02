import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
M = 1046527
NIL = -1
H = [None] * M
com = []
ch = []

for i in range(n):
    com_, ch_ = input().split()
    com.append(com_)
    ch.append(ch_)


table = str.maketrans({
'A':'1',
'C':'2',
'G':'3',
'T':'4',
})


def getChar(ch):
    return int(ch.translate(table))

def h1(key):
    return key % M
def h2(key):
    return 1 + (key % (M - 1))

def insert(ch):
    key = getChar(ch)
    i = 0
    while True:
        h = (h1(key) + i * h2(key)) % M
        if H[h] is None:
            H[h] = ch
            break
        else:
            i += 1

def find(ch):
    key = getChar(ch)
    i = 0
    while True:
        h = (h1(key) + i * h2(key)) % M
        if H[h] == ch:
            return 1
        elif H[h] is None:
            return 0
        else:
            i += 1


for i in range(n):
    if com[i][0] == 'i':
        insert(ch[i])
    else:
        if find(ch[i]):
            print('yes')
        else:
            print('no')
