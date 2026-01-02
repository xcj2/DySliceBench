def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def coprime(a, b) : 
    return (gcd(a, b) == 1) 

def make_div(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return sorted(divisors)

def count(arr):
    ans = set()
    for i in arr:
        if i == 1:
            ans.add(i)
            continue
        else:
            flag = 1
            for j in ans:
                if j != 1:
                    if (i % j) == 0:
                        flag = 0
                        break
            if flag == 1:
                ans.add(i)
    return(len(ans))

A,B = list(map(int,input().split()))
gcd_ab = gcd(A,B)
arr = make_div(gcd_ab)
n = len(arr)
print(count(arr))