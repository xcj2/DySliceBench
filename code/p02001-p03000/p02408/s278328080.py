import bisect,collections,copy,itertools,math,string
def I(): return int(input())
def S(): return input()
def LI(): return list(map(int,input().split()))
def SI(): return list(input().split())
##################################################
def main(N,C):
    SHCD = 'SHCD'
    _52card = [[0]*13 for _ in range(4)]
    for x in C:
        x1,x2 = x[0],int(x[1])
        _52card[SHCD.index(x1)][x2-1] = 1
    for i,x in enumerate(_52card):
        for j in range(13):
            if x[j]==0:
                print(SHCD[i],j+1)
    
N = I()
C = [SI() for _ in range(N)]
main(N,C)
