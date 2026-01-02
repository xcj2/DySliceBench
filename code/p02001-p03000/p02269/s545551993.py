import hashlib
from sys import stdin

def insert(v, B):
    key = hashlib.md5(v.encode("utf-8")).hexdigest()
    B[key] = v

def search(v, B):
    key = hashlib.md5(v.encode("utf-8")).hexdigest()
    if key in B:
        return key
    else:
        return 0

def read_and_print_word_dict(n):
    B = {}
    for _ in range(n):
        cmd = stdin.readline().strip().split()
        if cmd[0] == 'insert':
            insert(cmd[1], B)
        elif cmd[0] == 'find':
            res = search(cmd[1], B)
            if res == 0:
                print("no")
            else:
                print("yes")

n = int(input())
read_and_print_word_dict(n)
