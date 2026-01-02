def hash(v):
    return v % 100001

def insert(hashTable, value):
    key = hash(value)
    if hashTable[key] == None:
        hashTable[key] = [value]
    else:
        hashTable[key].append(value)

def find(hashTable, value):
    key = hash(value)
    if hashTable[key] == None:
        return False
    else:
        for val in hashTable[key]:
            if val == value:
                return True
    return False

def convert(string):
    res = ''
    for s in string:
        res += str(ord(s))
    return int(res)

n = int(input())
hashTable = [None] * 10**6
for i in range(n):
    com, val = input().split()
    val = convert(val)
    if com == 'insert':
        insert(hashTable, val)
    else:
        print('yes') if find(hashTable, val) else print('no')
