n=int(input())
dice=[input().split() for i in range(n)]
def E(ls):
    ls=[ls[3],ls[1],ls[0],ls[5],ls[4],ls[2]]
    return ls

def N(ls):
    ls=[ls[1],ls[5],ls[2],ls[3],ls[0],ls[4]]
    return ls

def R(ls):
    ls=[ls[0],ls[2],ls[4],ls[1],ls[3],ls[5]]
    return ls
    
def same(d1,d2):
    d1_ls=[d1,]
    for i in range(3):
        d1=E(d1)
        d1_ls.append(d1)
    d1=E(d1)
    d1=N(d1)
    d1_ls.append(d1)
    d1=N(N(d1))
    d1_ls.append(d1)
    for i in range(6):
        d=d1_ls[i]
        for j in range(3):
            d=R(d)
            d1_ls.append(d)
    if d2 in d1_ls:
        return True
    else:
        return False
k=0
for i in range(n):
    for j in range(i+1,n):
        if same(dice[i],dice[j]):
            k+=1
            break 
    else:continue    
    break
if k==1:
    print('No')
else:
    print('Yes')
