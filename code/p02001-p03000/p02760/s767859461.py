A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))

N = int(input())
bs = [int(input()) for _ in range(0, N)]

ans1 = [0, 0, 0]
ans2 = [0, 0, 0]
ans3 = [0, 0, 0]

def bingo_column():
    return ans1 == [1,1,1] or ans2 == [1,1,1] or ans3 == [1,1,1]

def bingo_row():
    if ans1[0] == 1 and ans2[0] == 1 and ans3[0] == 1:
        return True
    if ans1[1] == 1 and ans2[1] == 1 and ans3[1] == 1:
        return True
    if ans1[2] == 1 and ans2[2] == 1 and ans3[2] == 1:
        return True
    
    return False

def bingo_naname():
    if ans1[0] == 1 and ans2[1] == 1 and ans3[2] == 1:
        return True
    if ans1[2] == 1 and ans2[1] == 1 and ans3[0] == 1:
        return True
    return False

bingo = False
for b in bs:
    if b in A1:
        ix = A1.index(b)
        ans1[ix] = 1
    if b in A2:
        ix = A2.index(b)
        ans2[ix] = 1
    if b in A3:
        ix = A3.index(b)
        ans3[ix] = 1

    if bingo_column():
        bingo = True
    if bingo_row():
        bingo = True
    if bingo_naname():
        bingo = True

if bingo: 
    print('Yes')
else:
    print('No')