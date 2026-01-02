dice1=list(map(int,input().split()))
dice2=list(map(int,input().split()))

def E(ls):
    ls=[ls[3],ls[1],ls[0],ls[5],ls[4],ls[2]]
    return ls

def N(ls):
    ls=[ls[1],ls[5],ls[2],ls[3],ls[0],ls[4]]
    return ls

def R(ls):
    ls=[ls[0],ls[2],ls[4],ls[1],ls[3],ls[5]]
    return ls
    
dice1_ls=[dice1,]

for i in range(3):
    dice1=E(dice1)
    dice1_ls.append(dice1)
dice1=E(dice1)
dice1=N(dice1)
dice1_ls.append(dice1)
dice1=N(N(dice1))
dice1_ls.append(dice1)
for i in range(6):
    dice=dice1_ls[i]
    for j in range(3):
        dice=R(dice)
        dice1_ls.append(dice)
if dice2 in dice1_ls:
    print('Yes')
else:
    print('No')

