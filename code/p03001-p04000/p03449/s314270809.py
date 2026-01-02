def a():return input()#s
def ai():return int(input())#a,n or k
def ma():return map(int, input().split())#a,b,c,d or n,k
def ms():return map(str, input().split())#,a,b,c,d
def lma():return list(map(int, input().split()))#x or y
def lms():return list(map(str, input().split()))#x or y
a = ai()
z = lma()
y = lma()
x = [z,y]
k = []
l = 0
s = 0
sm = 0
M = 0
for j in range(a):
    l = 0
    sm = 0
    for i in range(a):
        sm+= x[l][i]
        if s == i:
            l+=1
            #print(l,i,j)
            sm+= x[l][i]
    s+=1
    M = max(M,sm)
print(M)
        