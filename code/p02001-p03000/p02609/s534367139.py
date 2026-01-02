# -*- coding: utf-8 -*-
import math

N = int(input())
X = list(input())
X = list(map(int, X))

def num_to_X(num):
    new_X = []
    new_N = int(math.log(num,2))+1
    for i in range(new_N):
        new_X.append(num>>i&1)
    return new_X[::-1]

def X_to_num(X):
    value = 0
    X = X[::-1]
    for i in range(len(X)):
        value += X[i]*pow(2,i)
    return value

def mode(X, mod):
    X = X[::-1]
    next_X = 0
    mod_2_i = 1
    for i in range(len(X)):
        next_X = (next_X+(X[i]*mod_2_i))%mod
        mod_2_i = (mod_2_i*2)%mod
    return next_X

def f(N, X, k):
    mod = sum(X)
    next_X = mode(X,mod)
    if next_X == 0:
        return k+1
    else:
        new_X = num_to_X(next_X)
        return f(len(new_X), new_X, k+1)

base_mod = sum(X)
# base_modが1なら, 操作は0回.
if base_mod == 1:
    for i in range(N):
        # 100 -> 000
        if X[i] == 1:
            print(0)
        # 100 -> 110
        elif i != N-1:
            print(1)
        # 100 -> 101
        else:
            print(2)
    exit(0)

plus_amari = mode(X, base_mod+1)
# print(X_to_num(X), base_mod+1, X_to_num(X)%(base_mod+1), plus_amari)
minus_amari = mode(X, base_mod-1)
# print(X_to_num(X), base_mod-1, X_to_num(X)%(base_mod-1), minus_amari)

results = []
modplus_2_i = 1
modminus_2_i = 1
X_hanten = X[::-1]

# print('----')
# print(X)
# print('----')

for i in range(N):
    # modが増えるパターン
    if X_hanten[i] == 0:
#         now_num = X_to_num(X)+pow(2,i)
#         now_mod = base_mod+1
        amari = (plus_amari+modplus_2_i)%(base_mod+1)
    else:
#         now_num = X_to_num(X)-pow(2,i)
#         now_mod = base_mod-1
        amari = (minus_amari-modminus_2_i)%(base_mod-1)
#     print(now_num, now_mod, now_num%now_mod,amari)

    if amari != 0:
        new_X = num_to_X(amari)
        results.append(f(len(new_X),new_X,1))
    else:
        results.append(1)

    modplus_2_i = (modplus_2_i*2)%(base_mod+1)
    modminus_2_i = (modminus_2_i*2)%(base_mod-1)

# print('---')
for result in results[::-1]:
    print(result)