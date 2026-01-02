import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
INF = 1000000000000

h,w,k = LI()
c = [S() for _ in range(h)]

result = 0
for i in range(1 << h):
    for j in range(1 << w):
        count = 0
        for y in range(h):
            if(i & (1 << y)):
                for x in range(w):
                    if(j & (1 << x)):
                        if(c[y][x] == '#'):
                            count += 1
        if(count == k):
            result += 1

print(result)