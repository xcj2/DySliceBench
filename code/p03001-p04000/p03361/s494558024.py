#ABC096-C
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return list(input())
h,w=IL()
S=[S() for i in range(h)]
ret=True
#grid周り探索
for i in range(h):
    for j in range(w):
        if S[i][j]==".":
            continue
        ans=False
        for ti in [-1,1]:
            if 0<=i+ti<h:
                if S[i+ti][j]=="#":
                    ans=True
        for tj in [-1,1]:
             if 0<=j+tj<w:
                if S[i][j+tj]=="#":
                    ans=True
        if not ans:
            ret=False
if ret:
    print("Yes")
else:
    print("No")