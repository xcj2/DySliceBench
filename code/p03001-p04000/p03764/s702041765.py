MOD = 1000000007
def hoge(a):
    b = a//2
    return (b*(b+1) + (a%2)*(b+1))%MOD
def power(a):
    return (a*a)%MOD
def abss(a):
    if a<0:
      return -a
    else:
      return a
n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
dx = []
dy = []
n-=1
m-=1
for i in range(n):
    dx.append(x[i+1]-x[i])
for i in range(m):
    dy.append(y[i+1]-y[i])
cx = hoge(n)
cy = hoge(m)
sx = 0
sy = 0
for i in range(n):
    if n%2==1:
        sx += dx[i]*(cx-power(abss(i-n//2)))
    else:
        if i<(n//2):
            sx += dx[i]*(cx-(n//2-i-1)*(n//2-i))
        else:
            sx += dx[i]*(cx-(i-n//2)*(i-n//2+1))
    sx%=MOD
for i in range(m):
    if m%2==1:
        sy += dy[i]*(cy-power(abss(i-m//2)))
    else:
        if i<(m//2):
            sy += dy[i]*(cy-(m//2-i-1)*(m//2-i))
        else:
            sy += dy[i]*(cy-(i-m//2)*(i-m//2+1))
    sy%=MOD
ans = (sx*sy)%MOD
if ans<0:
    ans+=MOD
print(ans)