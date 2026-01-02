# 横チェック
def yoko(bingo,b):
    i,j = 0,0
    isbingo = False
    for i in [0,1,2]:
        for j in [0,1,2]:
            if bingo[i][j] in b:
                if j==2:
                    return True
            else:
                break
    return False

def tate(bingo,b):
    i,j = 0,0
    isbingo = False
    for j in [0,1,2]:
        for i in [0,1,2]:
            if bingo[i][j] in b:
                if i==2:
                    return True
            else:
                break
    return False

def naname(bingo,b):
    i,j = 0,0
    isbingo = False
    for i,j in zip([0,1,2],[0,1,2]):
        if bingo[i][j] in b:
            if i==2:
                return True
        else:
            break
    for i,j in zip([0,1,2],[2,1,0]):
        if bingo[i][j] in b:
            if i==2:
                return True
        else:
        	break
    return False

row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
n = int(input())
i = 0
b = []
while(i < n):
  b.append(int(input()))
  i += 1

bingo = []
bingo.append(row1)
bingo.append(row2)
bingo.append(row3)
if (tate(bingo,b))|(yoko(bingo,b))|(naname(bingo,b)):
    print('Yes')
else:
    print('No')