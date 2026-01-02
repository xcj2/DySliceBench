import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N,M,V,P = MI()
A = [0] + LI()
A.sort()


def f(i):  # i番目の問題が採用されうるか
    a = A[i]
    v = V-i
    if A[-P] > a+M:
        return False
    v -= P-1
    if sum(a+M-A[j] for j in range(i+1,N-P+2)) >= M*v:
        return True
    return False


left = 0
right = N
while left + 1 < right:
    mid = (left + right)//2
    if f(mid):
        right = mid
    else:
        left = mid

print(N+1-right)
