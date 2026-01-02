def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


A = [LMI() for _ in range(3)]
N = I()
B = [I() for _ in range(N)]

bingo = [[False] * 3 for _ in range(3)]

for b in B:
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                bingo[i][j] = True
if all(bingo[0]) or all(bingo[1]) or all(bingo[2]):
    print('Yes')
elif all(row[0] for row in bingo) or all(row[1] for row in bingo) or all(row[2] for row in bingo):
    print('Yes')
elif bingo[0][0] and bingo[1][1] and bingo[2][2]:
    print('Yes')
elif bingo[0][2] and bingo[1][1] and bingo[2][0]:
    print('Yes')
else:
    print('No')