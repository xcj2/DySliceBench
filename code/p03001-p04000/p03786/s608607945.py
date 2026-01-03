import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
A = [0] + LI()
A.sort()


def f(n):  # 大きさが小さい方からn番目の生き物の色が、最後に残りうるか
    a = sum(A[i] for i in range(1,n+1))
    for i in range(n+1,N+1):
        if a*2 >= A[i]:
            a += A[i]
        else:
            return False
    return True


left = 0  # ng
right = N  # ok
while left + 1 < right:
    mid = (left + right)//2
    if f(mid):
        right = mid
    else:
        left = mid

print(N-right+1)
