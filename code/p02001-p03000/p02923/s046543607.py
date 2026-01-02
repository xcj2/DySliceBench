#インポート
import sys

#入力用
def ILI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def ISI(): return map(int, sys.stdin.readline().rstrip().split())
def II(): return int(sys.stdin.readline().rstrip())
def ISS(): return sys.stdin.readline().rstrip().split()
def IS(): return sys.stdin.readline().rstrip()

N = II()
H = ILI()
max = 0
cnt = 0
for i in range(N-1):
    if H[i] >= H[i+1]:
        cnt += 1
        if max < cnt:
            max = cnt
    else:
        if max < cnt:
            max = cnt
        cnt = 0
print(max)