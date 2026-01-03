import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,K = MI()
D = LI()

A = []  # 使ってよい数字
for i in range(10):
    if not i in D:
        A.append(i)

def f(x):
    if x <= max(A):
        for i in range(10-K):
            if A[i] >= x:
                return A[i]
    else:
        if x % 10 > max(A):
            return 10*f(x//10+1)+min(A)
        else:
            for i in range(10-K):
                if A[i] >= x % 10:
                    a = A[i]
                    break
            return min(10*f(x//10)+a,10*f(x//10+1)+min(A))

print(f(N))