import collections
N = int(input())

def make_divisors(n):
    divisors_set=set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            divisors_set.add(i)
            divisors_set.add(n//i)
    divisors_list=list(divisors_set)
    divisors_list.sort()
    return divisors_list

def make_primes(n):
    primes_list=[]
    while n % 2 == 0:
        primes_list.append(2)
        n = n//2
    f = 3
    while f * f <= n:
        if n % f == 0:
            primes_list.append(f)
            n = n//f
        else:
            f += 2
    if n != 1:
        primes_list.append(n)
    return primes_list

def cnt75(d):
    ans = 0
    for key in d.keys():
        if d[key] >= 75-1:
            ans += 1
    return ans

def cnt25_3(d):
    ans25 = 0
    ans3 = 0
    for key in d.keys():
        if d[key] >= 25-1:
            ans25 += 1
        elif d[key] >= 3-1:
            ans3 += 1
    #return ans25*(ans25-1+ans3)-(ans25*(ans25-1) )//2
    return ans25 * (ans25+ans3-1)

def cnt15_5(d):
    ans15 = 0
    ans5 = 0
    for key in d.keys():
        if d[key] >= 15-1:
            ans15 += 1
        elif d[key] >= 5-1:
            ans5 += 1
    #return ans15*(ans15-1+ans5)-(ans15*(ans15-1) )//2
    return ans15*(ans15+ans5-1)


def frac(n):
    if n == 1:
        return 1
    else:
        return n*frac(n-1)

def cnt5_5_3(d):
    ans5 = 0
    ans3 = 0
    for key in d.keys():
        if d[key] >= 5-1:
            ans5 += 1
        elif d[key] >= 3-1:
            ans3 += 1
    #return (ans5*(ans5-1))/2*ans3 + frac(ans5)//frac(2)//frac(ans5-2)
    return ans5*(ans5-1)*(ans5+ans3-2)//2 


#print( len(make_divisors(1*2*3*4*5*6*7*8*9*10) )) 
#cnt=0
#print(make_primes(6))
primes=[]
for i in range(1,N+1):
    #cnt+=len(make_primes(i))
    primes.extend(make_primes(i))
    #print(i,len(make_primes(i)))
    #print(make_primes(i))
#print(cnt)
#print(len(primes))
c=collections.Counter(primes)
#print(c)
print(cnt75(c)+cnt25_3(c)+cnt15_5(c)+cnt5_5_3(c) )
#print(2**8 * 3**4 * 5**2 * 7 )

