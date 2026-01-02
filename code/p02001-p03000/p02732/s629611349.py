import bisect,collections,copy,itertools,math,string
def I(): return int(input())
def S(): return input()
def LI(): return list(map(int,input().split()))
def LS(): return list(input().split())
##################################################
N = I()
A = LI()
_123 = [0]*N
_123count = [0]*N
for x in A:
    _123[x-1] += 1
_123copy = copy.copy(_123)
_123copy.sort(reverse=True)
_count = {}
for i,x in enumerate(_123copy):
    if x==0:
        break
    if x==1:
        _123count[i] = 0
    elif i!=0 and _123copy[i]==_123copy[i-1]:
        _123count[i] = _123count[i-1]
    else:
        _123count[i] = math.factorial(x)//((math.factorial(x-2))*(math.factorial(2)))
        _count[x] = _123count[i]
_sum = sum(_123count)
for x in A:
    temp = _123[x-1]-1
    if temp<=0:
        print(_sum)
    elif temp==1:
        print(_sum-1)
    else:
        if (temp+1) in _count:
            tempminus = _count[temp+1]
        else:
            tempminus = math.factorial(temp+1)//((math.factorial(temp-1))*(math.factorial(2)))
            _count[temp+1] = tempminus
        if (temp) in _count:
            tempplus = _count[temp]
        else:
            tempplus = math.factorial(temp)//((math.factorial(temp-2))*(math.factorial(2)))
            _count[temp] = tempplus
        print(_sum-tempminus+tempplus)
