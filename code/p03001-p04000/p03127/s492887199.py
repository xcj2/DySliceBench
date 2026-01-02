def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

from collections import deque
N = INT()
A = LI()
A.sort()

while True:
    mod = A[0]
    flg = True
    ans = A[0]
    tmp = deque([A[0]])
    
    if ans == 1:
        print(ans)
        break
    
    for i in range(1, len(A)):
        A[i] %= mod

        if A[i] != 0 and flg:
            flg = False
        
        if A[i] == 0:
            continue
        tmp.append(A[i])
        
    if flg:
        print(ans)
        break
    
    A = sorted(tmp)