MAX_INT = int(10e10)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

H,W,N = IL()
Sr,Sc = IL()
s = S()
t = S()

U = s.count("U")
D = s.count("D")
L = s.count("L")
R = N - (U+D+L)

if U >= Sr:
    cnt = Sr
    for i in range(N):
        if s[i] == "U":
            cnt -= 1
        if cnt == 0:
            print("NO")
            exit()
        if t[i] == "D":
            cnt = min(cnt+1,H)

if D >= H-Sr+1:
    cnt = Sr
    for i in range(N):
        if s[i] == "D":
            cnt += 1
        if cnt == H+1:
            print("NO")
            exit()
        if t[i] == "U":
            cnt = max(cnt-1,1)

if L >= Sc:
    cnt = Sc
    for i in range(N):
        if s[i] == "L":
            cnt -= 1
        if cnt == 0:
            print("NO")
            exit()
        if t[i] == "R":
            cnt = min(cnt+1,W)

if R >= W-Sc+1:
    cnt = Sc
    for i in range(N):
        if s[i] == "R":
            cnt += 1
        if cnt == W+1:
            print("NO")
            exit()
        if t[i] == "L":
            cnt = max(cnt-1,1)

print("YES")