n = int(input())
vec = []
for i in range(n):
    vec += [list(map(int, input().split()))]
vec += [vec[0]]
 
def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]
def ab(a, b):
    c = (b[0]-a[0],b[1]-a[1])
    return c
def dot(a, b):
    n = len(a)
    if n != len(b):
        return None
    ans = 0
    for i, j in zip(a, b):
        ans += i*j
    return ans

def check(a, b):
    if abs(cross(a, b)) < pow(10,-8) and dot(a,b)<pow(10,-8):
        return 1
    else:
        return 0
    
def contain():
    x = 0
    p = list(map(int, input().split()))
    for a,b in zip(vec[:-1],vec[1:]):
        a = ab(p,a)
        b = ab(p,b)
        if check(a, b) == 1:
            print(1)
            return 
        if a[1] > b[1]:
            a, b = b, a
        if a[1] < pow(10,-8) and b[1] > pow(10,-8) and cross(a, b) > 0:
            x += 1 
        
    if x%2==1:print(2)
    else:print(0)
k = int(input()) 
for i in range(k):
    contain()
