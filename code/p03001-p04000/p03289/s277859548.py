# coding: utf-8

def pHead(S):
    if S[0] != "A": return False
    return True

def getMid(S):
    return S[2:-1]

def pMid(S):
    mid = getMid(S)
    if "C" not in mid: return False
    if mid.count("C") > 1: return False
    return True

def getRest(S):
    mid = getMid(S)
    tmp = S[1] + mid.replace("C", "") + S[-1]
    return tmp

def solve(S):
    if not pHead(S):
        return "WA"
    if not pMid(S):
        return "WA"
    if not getRest(S).islower():
        return "WA"
    return "AC"

if __name__ == "__main__":
    S = input()
    print(solve(S))
