def up(x,y):
    if(y-1<0):return 0
    if a[y-1][x]=="#":return 1
    else:return 0
def down(x,y):
    if(y+1>h-1):return 0
    if a[y+1][x]=="#":return 1
    else:return 0
def right(x,y):
    if(x+1>w-1):return 0
    if a[y][x+1]=="#":return 1
    else:return 0
def left(x,y):
    if(x-1<0):return 0
    if a[y][x-1]=="#":return 1
    else:return 0

def upleft(x,y):
    if(y-1<0):return 0
    if(x-1<0):return 0
    if a[y-1][x-1]=="#":return 1
    else:return 0
def downleft(x,y):
    if(x-1<0):return 0
    if(y+1>h-1):return 0
    if a[y+1][x-1]=="#":return 1
    else:return 0
def upright(x,y):
    if(y-1<0):return 0
    if(x+1>w-1):return 0
    if a[y-1][x+1]=="#":return 1
    else:return 0
def downright(x,y):
    if(y+1>h-1):return 0
    if(x+1>w-1):return 0
    if a[y+1][x+1]=="#":return 1
    else:return 0

h,w=map(int,input().split())
a=[[i for i in input()] for j in range(h)]

for y in range(h):
    for x in range(w):
        if a[y][x]!="#":
            p=up(x,y)+down(x,y)+left(x,y)+right(x,y)+upright(x,y)+downright(x,y)+upleft(x,y)+downleft(x,y)
            print(p,end="")
        else:print("#",end="")
    print()