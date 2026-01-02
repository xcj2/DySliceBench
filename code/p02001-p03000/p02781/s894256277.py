n = int(input())
k = int(input())

def one(n):
    l = len(str(n))
    ans = 9 * (l-1)
    ans += n//(10**(l-1))
    return ans

def two(n):
    l = len(str(n))
    if l == 1:
        ans = 0
    elif l == 2:
        ans = (n//10-1) *9 + n%10
    else:
        ans =   81 * (l-1) * (l-2) // 2
        t = n % (10**(l-1))
        ans += one(t) + one(10**(l-1)-1)* (n// (10**(l-1))-1)
    return ans

def three(n):
    l = len(str(n))
    if l <= 2:
        ans = 0
    elif l == 3:
        ans = (n//100-1) * two(99) + two( n % 100 )
    else:
        ans = 729 * (l-1) * (l-2) * (l-3) // 6
        t = n % (10**(l-1))
        ans += two(t) + two(10**(l-1)-1)* (n// (10**(l-1))-1)
    return ans

if k == 1:
    ans = one(n)
if k == 2:
    ans = two(n)
if k == 3:
    ans = three(n)

print(ans)