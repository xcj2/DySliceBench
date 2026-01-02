#インポート
import sys

#入力用
def ILI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def ISI(): return map(int, sys.stdin.readline().rstrip().split())
def II(): return int(sys.stdin.readline().rstrip())
def ISS(): return sys.stdin.readline().rstrip().split()
def IS(): return sys.stdin.readline().rstrip()


dx = [-1,  0,  1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1,  0, 0,  1, 1, 1]
H, W = ISI()
l = [list(IS()) for i in range(H)]
for i in range(H):
    for j in range(W):
        if l[i][j] != "#":
            cnt = 0
            for d in range(8):
                ni = i + dy[d]
                nj = j + dx[d]
                if 0 > ni or ni >= H: continue
                if 0 > nj or nj >= W: continue
                if l[ni][nj] == "#":
                    cnt += 1
            l[i][j] = str(cnt)
for i in range(H):
    print("".join(l[i]))