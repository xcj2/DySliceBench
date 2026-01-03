from collections import deque

h,w=map(int,input().split())
a=[list(input()) for j in range(h)]
x=[0,0]#xが"#"を仮定

def next_point_is_ok1(i,j):
    global a,h
    if i < h-1:
        return a[i+1][j]=="#"
    else:
        return False

def next_point_is_ok2(i,j):
    global a,w
    if j < w-1:
        return a[i][j+1]=="#"
    else:
        return False


def next_points():
    global x,a
    #print(x)
    if x==[h-1,w-1]:
        #print(0)
        if a == [["." for i in range(w)] for j in range(h)]:
            print("Possible")
        else:
            print("Impossible")
    elif next_point_is_ok1(x[0],x[1]):
        #print(1)
        x[0]+=1
        a[x[0]][x[1]]="."
        next_points()
    elif next_point_is_ok2(x[0],x[1]):
        #print(2)
        x[1]+=1
        a[x[0]][x[1]]="."
        next_points()
    else:
        #print(3)
        print("Impossible")

#print(a)
if a[0][0]==".":
    print("Impossible")
else:
    a[0][0]="."
    next_points()
