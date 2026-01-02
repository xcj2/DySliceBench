def divisors(n):
    divs = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            divs |= {i, n//i}
    return sorted(divs)

def gcd(n,m):
    if m == 0:
        return n
    else:
        return gcd(m, n%m)

def is_disjoint(n,m):
    return gcd(n,m) == 1

def appendable(list, n):
    return all(is_disjoint(l, n) for l in list)

#O(n**2)!
def filter_disjoint(divisors):
    list = []
    for d in divisors:
        if appendable(list, d):
            list.append(d) 
    return list


a,b = list(map(int, input().split()))

filterd = filter_disjoint(divisors(gcd(a,b)))
print(len(filterd))