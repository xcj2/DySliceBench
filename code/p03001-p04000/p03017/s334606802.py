def passable(road):
    n=len(road)
    for i in range(n-1):
        block=road[i:i+2]
        if block=='##':
            return False
    return True

def safe_place(road):
    n=len(road)
    for i in range(n-2):
        block=road[i:i+3]
        if block=='...':
            return i+1
    return -1

def passEach(A,B,C,D,road):
    if passable(road[A:C+1]) and passable(road[B:D+1]):
        return True
    else:
        return False

def judge(A,B,C,D,S):
    if C<D:
        return passEach(A,B,C,D,S)
    else:
        S2=S[:B]+'#'+S[B+1:]
        if passable(S2[A:C+1]) and passable(S[B:D+1]):
            return True
        S3=S[:D]+'#'+S[D+1:]
        if passable(S3[A:C+1]) and passable(S[B:D+1]):
            return True
        safePlace=safe_place(S[B:D+1])
        if safePlace!=-1 and passEach(A,B,C,safePlace+B,S) and passEach(A,safePlace+B,C,D,S):
            return True
    return False

N,A,B,C,D=map(int,input().split())
S=input()
if judge(A-1,B-1,C-1,D-1,S):
    print('Yes')
else:
    print('No')