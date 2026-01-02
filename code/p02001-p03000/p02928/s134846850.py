mod = 10**9+7
n , k = map(int,input().split())
arr =[ int(i) for i in input().split() ]
cnt_tot = [ 0 for i in range(2005) ]
bit = [ 0 for i in range(2005) ]
def sum(r):
    global bit
    ret = 0
    while r >= 0:
        ret += bit[r]
        r = ( r & (r+1) ) - 1
    return ret

def add(idx, delta):
    global bit
    while idx < 2005:
        bit[idx] += delta
        idx = idx | (idx+1)

def sum2(l,r):
    return sum(r) - sum(l-1)

for i in range(n):
    cnt_tot[arr[i]] += 1
for i in range(1,2005):
    cnt_tot[i] += cnt_tot[i-1]

ans = 0
full = (k-1) * (k) * pow(2,mod-2,mod)
for i in range(n):
    ans += (n-cnt_tot[arr[i]])
ans = ans * full
# print(ans)
other = 0
for i in range(n):
    other += sum2(arr[i]+1,2004)
    add(arr[i],1)
other = other * k
# print(other)
ans += other

ans = ans % mod

print(ans)
