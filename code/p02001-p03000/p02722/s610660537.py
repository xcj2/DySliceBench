def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

def sousa(n, k):
    while n >= k:
        if n % k == 0:
            n = n // k
        else:
            n = n % k
    return n

N = int(input())
cnt = 0

if N == 2:
    print(1)
    exit()

divisors = make_divisors(N)
for i in divisors:
    if i == 1: continue
    if sousa(N, i) == 1:
        cnt += 1

lst = factorization(N-1)
tuika = 1
for i in range(len(lst)):
    tuika *= lst[i][1]+1
# cnt += len(make_divisors(N-1))-1
cnt += tuika-1
print(cnt)