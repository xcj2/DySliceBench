import sys
 
# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())
 
def log(*args):
    print("DEBUG:", *args, file=sys.stderr)
 
def int_to_bits(x):
    return [ 1 if 2**i & x != 0 else 0 for i in range(60) ]
 
def inv(x, MOD):
    return pow(x, MOD-2, MOD)
 
MOD = 10**9+7
 
n,*A = get_all_int()
 
pow2    = [1] * 61
pow2mod = [1] * 61
for i in range(1,61):
    pow2[i] = pow2[i-1] * 2
    pow2mod[i] = pow2[i] % MOD
 
# ビットごとの出現回数 2**i
bits = [0] * 60
 
for a in A:
    for i in range(60):
        if pow2[i] & a != 0:
            bits[i] += 1
 
ans = 0
 
for a in A:
    for i in range(60):
        ans += pow2mod[i] * abs(bits[i] - (1 if pow2[i] & a != 0 else 0) *n)
 
print(ans*inv(2,MOD) % MOD)