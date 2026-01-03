import collections
def a():return input()#s
def ai():return int(input())#a,n or k
def ma():return map(int, input().split())#a,b,c,d or n,k
def ms():return map(str, input().split())#,a,b,c,d
def lma():return list(map(int, input().split()))#x or y
def lms():return list(map(str, input().split()))#x or y
k= []
l = []
f = 0
def say(i):return print("Yes" if i == 0 else "No")
def Say(i):return print("YES" if i == 0 else "NO")
a = ai()
x = lma()
k = [0]*a
s = 0
t = 0
for i in range(a):
    if i%2==0:
        k[s] = x[-1-i]
        s+=1
    else:
        k[-t-1] = x[-1-i]
        t+=1
s = str(k[0])
for i in range(1,a):
    s+=" "+str(k[i])
print(s)