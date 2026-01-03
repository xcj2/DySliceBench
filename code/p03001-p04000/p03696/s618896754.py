import sys

n = int(input())
s = input()

tries = []

def count(S):
    cnt = 0
    for i in S:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
    return cnt

def valid(S):
    cnt = 0
    for i in S:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True

def bt(S):
    cnt = count(S)
    if count(S) == 0 and valid(S):
        tries.append(S)
        return
    else:
        if cnt < 0:
            return bt("(" + S)
        else:
            return bt(S + ")")
bt(s)
print(min(tries))
