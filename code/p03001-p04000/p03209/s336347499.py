def total(n):
    return 2**(n+2)-3

def left(total,x):
    if x > (total+1)//2:
        return x-(total+1)//2
    else:
        return x
def pati(n):
    return 2**(n+1)-1

n,x = map(int,input().split())
num = []
p = []
for i in range(n-1):
    num.append(total(i))
for i in range(n+1):
    p.append(pati(i))


one = ["B","P","P","P","B"]
num.reverse()
eat = [0 for i in range(n+1)]

ans = 0
for i in range(n-1):
    if x == total(n-i):
        eat[n-i] += 1
        x = 0
    elif x > (total(n-i)+1)//2:
        eat[n-i-1] += 1
        x = left(total(n-i),x)
        ans += 1
    elif x == (total(n-i)+1)//2:
        eat[n-i-1] += 1
        eat[0] += 1
        x = 0
    else:
        x -= 1

for i in range(len(eat)):
    ans += eat[i]*p[i]
if 2<=x<=4:
    ans += x-1
elif x == 5:
    ans += 3
print(ans)