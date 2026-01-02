N = int(input())
a = []
b = []
c = []
for i in range(N):
    a += [list(map(int, input().split()))]
    
row = [1]*9
col = [1]*9
dops = [1]*16
dneg = [1]*16

def sett(x, y):
    row[y] = 0
    col[x] = 0
    dops[x+y] = 0
    dneg[y-x+7] = 0

def dsett(x, y):
    row[y] = 1
    col[x] = 1
    dops[x+y] = 1
    dneg[y-x+7] = 1
    
def paint(ans):
    pain = [["."]*8for _ in range(8)]
    for i, j in ans.items():
        pain[i][j] = "Q"
        print("".join(pain[i]))
    
cnt = 1
def serch(h):
    global cnt
    if h == 8:
        aa = 0
        for i, j in a:
            if ans[i] == j:
                aa += 1
        if aa == len(a):
            cnt = 0
            paint(ans)
            return
    for i in range(8):
        if row[h] and col[i] and dops[h+i] and dneg[h-i+7] and cnt:
            sett(i, h)
            ans[h] = i
            
            serch(h+1)
            
            dsett(i, h)
            del ans[h]

ans = {}          
serch(0) 

    
    
