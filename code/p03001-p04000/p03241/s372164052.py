#!/mnt/c/Users/moiki/bash/env/bin/python

N, M = list(map(int, input().split()))

# N splited by number of M 
import math
plist = [2]
for i in range(3, int(1e5+1)):
    ok = True
    for j in plist:
        if j > math.sqrt(i):
            break   
        elif i % j == 0:
            ok = False
            break
    if ok:
        plist.append(i)

# print(plist)

## 

prime_pair = {}

def cnt_power(n, p):
    if p < 2:
        raise "p is smaller than 2."
    if n >= p and n % p == 0:
        return 1 + cnt_power(int(n/p), p)
    else:
        return 0
        
def fac(N):
    global prime_pair
    for p in plist:
        if N % p == 0:  
            # print(N,p)
            # prime_pair[p = ] = (p, cnt_power(N, p))
            prime_pair[p] = cnt_power(N, p)

# print(fac(M))
fac(M)

import copy
divisor = []
init_nowpair = {}
for k in prime_pair:
    # print("prime pair: ", k, prime_pair[k])
    init_nowpair[k] = 0


def makedivisor(prime_pair, now_pair):
    # print(now_pair)
    multi = 1
    for np in now_pair:
        multi *= int(pow(np, now_pair[np]))
    #     print("\tmulti:", multi)
    # print("multi:", multi)
    if multi > M:
        return 
    else:
        if not multi in divisor:
            divisor.append(multi)
        else:
            return 
    

    for np in now_pair:
        if prime_pair[np] > now_pair[np]:
            now_pair2 = copy.deepcopy(now_pair)
            now_pair2[np] += 1
            makedivisor(prime_pair, now_pair2)
makedivisor(prime_pair, init_nowpair)            
divisor.sort()
# print(divisor)

maxx = 0
for d in divisor:
    if M % d == 0 and int(M/d) >= N:
        maxx = max(maxx, d)

print(maxx)
        
    
# for k in prime_pair:
#     print(k,prime_pair[k])





# maxx = 0
# maxlen = 0
# for i in range(3, int(1e9)):
#     if i % int(1e3) == 0:
#         print(i)
#         print(maxx, maxlen)

#     prime_pair = {}
#     fac(i)
#     maxlen = max(maxlen, len(prime_pair))
#     for k in prime_pair:
#         maxx = max(maxx, prime_pair[k])
    