A1 = list(map(int,input().split(' ')))
A2 = list(map(int,input().split(' ')))
A3 = list(map(int,input().split(' ')))
N = int(input())
B = [0]*N
for i in range(N):
    b = int(input())
    B[i]=b

marubatu = [[0,0,0],
[0,0,0],
[0,0,0]]

for b in B:
    for i,a1 in enumerate(A1):
        if b==a1:
            marubatu[0][i]=1
    for i,a2 in enumerate(A2):
        if b==a2:
            marubatu[1][i]=1
    for i,a3 in enumerate(A3):
        if b==a3:
            marubatu[2][i]=1

def tate():
    f = False
    for i in range(3):
        if (marubatu[i][0])and(marubatu[i][1])and(marubatu[i][2]==1):
            f=True
    return f

def yoko():
    f = False
    for i in range(3):
        if (marubatu[0][i])and(marubatu[1][i])and(marubatu[2][i]==1):
            f=True
    return f

def migisagari():
    f = False
    if (marubatu[0][0])and(marubatu[1][1])and(marubatu[2][2]==1):
        f=True
    return f

def hidarisagari():
    flag=False
    if (marubatu[0][2])and(marubatu[1][1])and(marubatu[2][0]==1):
        flag=True
    return flag

#print(marubatu)

f1 = tate()
f2 = yoko()
f3 = migisagari()
f4 = hidarisagari()

if f1 or f2 or f3 or f4:
    print('Yes')
else:
    print('No')