N = int(input())
X = input()

def popcount(n):
    return bin(n).count('1')

def process(n):
    return n % popcount(n)

def func(n):
    ret = 0
    while n > 0:
        n = process(n)
        ret += 1
    return ret

pcnt = X.count('1')
mods_plus = []
totalmod_plus = 0
tmp_plus = 1
pp = pcnt+1
mods_minus = []
totalmod_minus = 0
tmp_minus = 1
pm = pcnt-1
for c in reversed(X):
    if c == '1':
        totalmod_plus += tmp_plus
        totalmod_plus %= pp
    mods_plus.append(tmp_plus)
    tmp_plus = tmp_plus*2 % pp
    if pcnt != 1:
        if c == '1':
            totalmod_minus += tmp_minus
            totalmod_minus %= pm
        mods_minus.append(tmp_minus)
        tmp_minus = tmp_minus*2 % pm

for i in range(N):
    if X[i] == '1':
        if pcnt == 1:
            print(0)
        else:
            mod = mods_minus[-i-1]
            print(func((totalmod_minus - mod) % pm) + 1)
    else:
        mod = mods_plus[-i-1]
        print(func((totalmod_plus + mod) % pp) + 1)
