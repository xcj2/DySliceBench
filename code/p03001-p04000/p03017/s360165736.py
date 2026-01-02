def passable(road):
    n=len(road)
    for i in range(n-1):
        block=road[i:i+2]
        if block=='##':
            return False
    return True

def blank(road):
    n=len(road)
    for i in range(1,n-1):
        block=road[i-1:i+2]
        if block=='...':
            return True
    return False

def judge(A,B,C,D,S):
    if C<D:
        return passable(S[A:C+1]) and passable(S[B:D+1])
    else:
        return passable(S[A:C+1]) and passable(S[B:D+1]) and blank(S[B-1:D+2])
N,A,B,C,D=map(int,input().split())
S=input()
if judge(A-1,B-1,C-1,D-1,S):
    print('Yes')
else:
    print('No')