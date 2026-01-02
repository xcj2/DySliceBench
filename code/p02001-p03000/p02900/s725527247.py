def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

def gcd(x, y):
    if y==0:
        return x
    return gcd(y, x%y)

def lcm(x, y):
    return x//gcd(x, y)*y

A, B = map(int, input().split())
cd = make_divisors(gcd(A, B))
ans = []
for i in range(1, len(cd)):
    flag = True
    for j in range(len(ans)):
        if cd[i]%ans[j] == 0:
            flag = False
            break
    if flag:
        ans.append(cd[i])
print(len(ans)+1)