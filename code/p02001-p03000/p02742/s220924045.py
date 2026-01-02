import bisect,collections,itertools,math,numpy,string
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return list(map(int,input().split()))
##################################################
def main(H,W):
    if H==1 or W==1:
        return 1
    elif H%2==0 and W%2==0:
        return (H*W)//2
    elif H%2==0 and W%2==1:
        return (H//2)*(2*(W//2)+1)
    elif H%2==1 and W%2==0:
        return (2*(H//2)+1)*(W//2)
    else:
        return (H//2)*(2*(W//2)+1)+((W//2)+1)
    
H,W = LI()
print(main(H,W))