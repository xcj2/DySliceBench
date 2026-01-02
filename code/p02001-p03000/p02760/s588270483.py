a = input().split()
b = input().split()
c = input().split()
list_ans =(a,b,c)
N = int(input())
bingo_list=[]

for i in range(N):
    bingo = input()
    bingo_list.append(bingo)


#横ビンゴ判定
def bingo_row(p,q):
    row_total= 0
    #p 横のリスト　q 出た値のリスト
    for i in range(3):
        if p[i] in q:
            row_total +=1
        else:
            return False
    if row_total == 3:
        return True
#縦ビンゴ判定
def bingo_column(p,q,r,s):
    batu = 0
    #pqr横リスト　s bingo_list
    for i in range(3):
        
        if p[i]  in s and q[i] in s:
            if r[i] in s:
                return True
                break
            else:
                batu +=1 
        else:
            batu +=1
    if batu == 3:
        return False
#斜めビンゴ判定
def bingo_slash(p,q,r,s):
    if q[1] in s:
        if p[0] in s and r[2] in s:
            return True
        elif p[2] in s and r[0] in s:
            return True
        else:
            return False
    else:
        return False

    
total = 0
for i in list_ans:
    if bingo_row(i, bingo_list):
        print('Yes')
        break
    elif bingo_column(a,b,c,bingo_list):
        print('Yes')
        break
    elif bingo_slash(a,b,c,bingo_list):
        print('Yes')
        break
    else:
        total += 1
if total == 3:
    print('No')
                    