import sys
MAX_INT = int(10e12)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
s = S()

cnt = 0
for a in range(10):
    for b in range(10):
        n = 0
        ab = [a,b]
        for i in range(N):
            if int(s[i]) == ab[n]:
                n += 1
            if n == 2:
                for c in range(10):
                    for j in range(i+1,N):
                        if int(s[j]) == c:
                            cnt += 1
                            break
                else:
                    break
print(cnt)