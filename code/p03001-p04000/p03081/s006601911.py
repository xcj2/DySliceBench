import sys

input = sys.stdin.readline
N, Q = map(int,input().split())
s = input()
query = [list(input().split()) for i in range(Q)]

def leftOK(index):
    for q in query:
        if q[0] == s[index]:
            if q[1] == "L":
                index -= 1
            else:
                index += 1
        if index == -1:
            return True
        elif index == N:
            return False
    return False
    
def rightOK(index):
    for q in query:
        if q[0] == s[index]:
            if q[1] == "L":
                index -= 1
            else:
                index += 1
        if index == N:
            return True
        elif index == -1:
            return False
    return False
    
def nibutan(f,ng,ok):
    count = 0
    while abs(ok-ng) > 1:
        count += 1
        mid = (ok + ng)//2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok
    
left = nibutan(leftOK,N,-1)
right = nibutan(rightOK,-1,N)
print(right-left-1)