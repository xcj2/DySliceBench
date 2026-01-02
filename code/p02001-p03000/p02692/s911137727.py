def Int():
    return int(input())
def Ints():
    return map(int,input().split())
def IntList():
    return list(Ints())
def IntMat(N):
    return [IntList() for i in range(N)]

import sys

N,A,B,C = Ints()
            
QList = []
for i in range(N-1):
    QList.append(input())
QList.append(input())
#print(QList)
#print(QList[0]=='AB')
    
Ans = []
Wh = 1
now = 0

while now < N:
    q = QList[now]
    #print(A,B,C)
    if not (A>=0 and B>= 0 and C>=0):
        Wh = 0
        break
    if q=='AB':
        if A==0 and B==0:
            print('No')
            sys.exit()
        elif A==1 and B==1:
            if now==N-1:
                Ans.append('A')
                A += 1
                B -= 1
            else:
                nexq = QList[now+1]
                if nexq==q:
                    Ans.append('A')
                    A += 1
                    B -= 1
                elif nexq == 'AC':
                    Ans.append('A')
                    A += 1
                    B -= 1
                elif nexq == 'BC':
                    Ans.append('B')
                    B += 1
                    A -= 1
        else:
            if A<B:
                Ans.append('A')
                A += 1
                B -= 1
            else:
                Ans.append('B')
                B += 1
                A -= 1
    if q=='AC':
        if A==0 and C==0:
            print('No')
            sys.exit()
        elif A==1 and C==1:
            if now==N-1:
                Ans.append('A')
                A += 1
                C -= 1
            else:
                nexq = QList[now+1]
                if nexq==q:
                    Ans.append('A')
                    A += 1
                    C -= 1
                elif nexq == 'BC':
                    Ans.append('C')
                    C += 1
                    A -= 1
                elif nexq == 'AB':
                    Ans.append('A')
                    A += 1
                    C -= 1
        else:
            if A<C:
                Ans.append('A')
                A += 1
                C -= 1
            else:
                Ans.append('C')
                C += 1
                A -= 1
    if q=='BC':
        if B==0 and C==0:
            print('No')
            sys.exit()
        elif B==1 and C==1:
            if now==N-1:
                Ans.append('B')
                B += 1
                C -= 1
            else:
                nexq = QList[now+1]
                if nexq==q:
                    Ans.append('B')
                    B += 1
                    C -= 1
                elif nexq == 'AC':
                    Ans.append('C')
                    C += 1
                    B -= 1
                elif nexq == 'AB':
                    Ans.append('B')
                    B += 1
                    C -= 1
        else:
            if B<C:
                Ans.append('B')
                B += 1
                C -= 1
            else:
                Ans.append('C')
                C += 1
                B -= 1
    now += 1
                
if Wh==0:
    print('No')
else:
    print('Yes')
    for i in Ans:
        print(i)