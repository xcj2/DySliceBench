import sys

def h1(key):
    return key % M

def h2(key):
    return 1 + key % (M - 1)

def H(key, i):
    return (h1(key) + i * h2(key)) % M

def my_insert(dic, key):
    i = 0

    while 1:
        j = H(key, i)
        if dic[j] is None:
            dic[j] = key
            return j
        else:
            i += 1

def my_search(dic, key):
    i = 0

    while 1:
        j = H(key, i)
        if dic[j] == key:
            return True
        elif dic[j] is None or i >= M:
            return False
        else:
            i += 1

def str2int(s):
    res = s

    res = res.replace("A", "1")
    res = res.replace("C", "2")
    res = res.replace("G", "3")
    res = res.replace("T", "4")

    return int(res)

M = 1000003
dic = [None] * M

n = int(sys.stdin.readline())

for k in range(n):
    cmd, s = sys.stdin.readline().split()

    if cmd == "insert":
        my_insert(dic, str2int(s))
    else:
        print("yes" if my_search(dic, str2int(s)) else "no")