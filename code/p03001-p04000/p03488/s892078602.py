import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

s = lc()
x,y = li()


# F,Tコマンド圧縮
command = []
last = ""
com = ""
cnt = 0
for i, si in enumerate(s):
    if si != last:
        if i != 0:
            command.append((com, cnt))
        cnt = 1
        com = si
        last = si
    
    else:
        cnt += 1
        last = si
        
    if i == len(s)-1:
        command.append((com, cnt))
        
        
# コマンド処理
isx = 1
if command[0][0] == "F":
    x_cand = set([command[0][1]])
    y_cand = set([0])
    command = command[1:]
else:
    x_cand = set([0])
    y_cand = set([0]) 

for cmd, cnt in command:
    if cmd == 'F':
        if isx == 1:
            x_cand = set([xi+cnt for xi in x_cand]) | set([xi-cnt for xi in x_cand])
        elif isx == -1:
            y_cand = set([yi+cnt for yi in y_cand]) | set([yi-cnt for yi in y_cand])
        
    elif cmd == 'T':
        if cnt%2 == 1:
            isx *= -1
    
if x in x_cand and y in y_cand:
    print('Yes')
else:
    print('No')