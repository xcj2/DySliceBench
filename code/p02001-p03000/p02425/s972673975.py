def showBit(self):
    print("{:b}".format(data))

def bitCheck(n,i):
    return (int(bool(n&1<<i)))

def bitOn(n,i):
    return n|1<<i

def bitOff(n,i):
    return n&~(1<<i)

def bitFlip(n,i):
    return n^1<<i

def isbitAll(n):
    return int(bitCount(n)==64)

def isbitAny(n):
    return int(bitCount(n)>0)

def isbitNone(n):
    return int(bitCount(n)==0)

def bitCount(n):
    return bin(n).count('1')

n=0
q=int(input())
for i in range(q):
    qry=list(map(int,input().split()))
    if qry[0]==0:
        print(bitCheck(n,qry[1]))
    elif qry[0]==1:
        n=bitOn(n,qry[1])
    elif qry[0]==2:
        n=bitOff(n,qry[1])
    elif qry[0]==3:
        n=bitFlip(n,qry[1])
    elif qry[0]==4:
        print(isbitAll(n))
    elif qry[0]==5:
        print(isbitAny(n))
    elif qry[0]==6:
        print(isbitNone(n))
    elif qry[0]==7:
        print(bitCount(n))
    elif qry[0]==8:
        print(n)

