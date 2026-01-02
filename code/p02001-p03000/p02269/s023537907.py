import sys

def conv(s):
    patterns = [["A", "1"], ["C", "2"], ["G", "3"], ["T", "4"]]
    for i, j in patterns:
        s = s.replace(i, j)
    return int(s)

MAX_PAT = pow(4,12)

def h1(val):
    return val % MAX_PAT
    
def h2(val):
    return 1 + val % (MAX_PAT-1)

def h(val, i):
    return (h1(val) + i*h2(val)) % MAX_PAT

def insert(val, arr):
    i = 0
    while True:
        idx = h(val, i)
        if arr[idx] == "NIL":
            arr[idx] = val
            return idx
        else:
            i += 1

def find(val, arr):
    i = 0
    while True:
        idx = h(val, i)
        if arr[idx] == val:
            return True
        elif (arr[idx]=="NIL")|(i>=MAX_PAT):
            return False
        else:
            i += 1
    return

dictionary = ["NIL" for i in range(MAX_PAT)]
n = int(input())
for i in range(n):
    cmd, val = sys.stdin.readline().split()
#    cmd, val = input().split()
    val = conv(val)
    if cmd == "insert":
        if not find(val, dictionary):
            insert(val, dictionary)
    if cmd == "find":
        if find(val, dictionary):
            print("yes")
        else:
            print("no")

