import sys
input = sys.stdin.readline

n = int(input())

m = 1046527

H = [None]*m

table = str.maketrans({
'A':'1',
'C':'2',
'G':'3',
'T':'4',
})

# 文字から数値に変換
# https://qiita.com/tag1216/items/df6c93bdb823dd48af6c参照
def getChar(string):
    return int(string.translate(table))

# pythonでは12桁でもメモリを考えず動くのでgetKeyを実装していません。

def h1(key):
    return key % m

def h2(key):
    return 1 + (key % (m-1))

def find(string):
    i = 0
    key = getChar(string)
    while True:
        h = (h1(key) + i*h2(key))%m
        if H[h] == string:
            return 1
        elif H[h] is None:
            return 0
        else:
            i += 1

def insert(string):
    i = 0
    key = getChar(string)
    while True:
        h = (h1(key) + i*h2(key))%m
        if H[h] is None:
            H[h] = string
            break
        else:
            i += 1

for _ in range(n):
    com, string = input().split()
    if com[0] == 'i':
        insert(string)
    else:
        if find(string):
            print('yes')
        else:
            print('no')

