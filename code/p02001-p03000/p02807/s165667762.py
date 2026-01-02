n = int(input())
X = list(map(int, input().split()))

def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m

total = 0
min_sekisan = 1
mod = 10 ** 9 + 7
for i in range(1, n):
    min_sekisan *= i
    min_sekisan %= mod
#print(min_sekisan)

counter = 0
for i in range(n-1):
    counter += min_sekisan
    total -= (min_sekisan * X[i]) % mod
    min_sekisan *= i + 1
    min_sekisan *= mod_inv(i + 2, mod)
    min_sekisan %= mod
total += (X[n-1] * counter) % mod
print(total % mod)

"""
from collections import defaultdict as dd
import copy
def count(n):
    lis = [[[i for i in range(1, n + 1)], dd(int)]]
    while len(lis[0][0]) != 1:
        temp = []
        for nums, counter in lis:
            for i in range(len(nums)-1):
                new_dic = copy.deepcopy(counter)
                new_dic[nums[i]] -= 1
                new_dic[nums[i+1]] += 1
                temp.append([nums[:i] + nums[i+1:], new_dic])
        lis = temp
    return lis
#print(count(4))
#print(len(count(4)))

total = dd(int)
for lis, dic in count(7):
    for key, val in dic.items():
        total[key] += val
print(total)
"""