import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

H, W = mapint()
query = [list(input()) for _ in range(H)]

def check():
    for h in range(H):
        for w in range(W):
            if query[h][w]=='.':
                continue
            if h!=0 and query[h-1][w]=='#':
                continue
            if h<H-1 and query[h+1][w]=='#':
                continue
            if w!=0 and query[h][w-1]=='#':
                continue
            if w<W-1 and query[h][w+1]=='#':
                continue
            return False
    return True

if check():
    print('Yes')
else:
    print('No')