primes = [2]
def prime():
    c = 3
    while True:
        for i in primes:
            if i * i > c:
                primes.append(c)
                break
            if c % i == 0:
                break
            
        c += 1
        if c > 10**6:
            return


prime()

def check(a):
    if a == 1:
        return False
    for i in primes:
        if i * i > a:
            return True
        if a % i == 0:
            return False
        i += 1


#print('a')
def solve(a,d,n):
    while True:
        if check(a):
            n -= 1
            if n == 0:
                print(a)
                return 
        a += d 

while True:
    l = input().split(' ')
    a = int(l[0])
    d = int(l[1])
    n = int(l[2])
    if a == 0:
        break
    solve(a,d,n)
            


