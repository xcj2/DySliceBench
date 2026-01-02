def a():return input()#s
def ai():return int(input())#a,n or k
def ma():return map(int, input().split())#a,b,c,d or n,k
def ms():return map(str, input().split())#,a,b,c,d
def lma():return list(map(int, input().split()))#x or y
def lms():return list(map(str, input().split()))#x or y
k= [0]
l = [0]
m=[]
co = range(1,10**5+2,2)
ce = range(0,10**5+2,2)
f = 1
def say(i):return print("Yes" if i == 1 else "No")
def Say(i):return print("YES" if i == 0 else "NO")
#def rep(i):return for i in range()
def addarray(k,l):
    for i in range(n):
        a ,b,c = map(int,input().split())
        k.append(a)
        l.append(b+c)
n = ai()
addarray(k,l)
for i in range(1,n+1):
    t = k[i]-k[i-1]
    if t%2==1 and abs(l[i]-l[i-1]) in co[:t//2+1]:
        f = 1
    elif t%2==0 and abs(l[i]-l[i-1]) in ce[:t//2+1]:
        f = 1
    else:
        f = 0
        break
say(f)
    