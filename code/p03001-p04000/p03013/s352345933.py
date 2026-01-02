import math

N,M = map(int,input().split(' '))
An = [ int(input()) for _ in range(M)]

'''
factorial_list = [1] * (N+1)
for i in range(1,N+1):
    factorial_list[i] = factorial_list[i-1] * i

def combinations_count(n, r):
    return factorial_list[n] // (factorial_list[n - r] * factorial_list[r])
'''

feruma_list = [1] * (N+1)
for i in range(2,N+1):
    feruma_list[i] = feruma_list[i-2] + feruma_list[i-1]


def nCk(n, k):
    ret = 1
    mo = 10**9 + 7
    for i in range(k):
        ret = ret * (n - i) * pow(i + 1, mo - 2, mo) % mo
    return ret

def one_two_comb(N):
    two_n = N//2
    comb_list = []
    for i in range(1,two_n+1):
        comb_list.append([N-i,i])
    return comb_list

def sum_comb(comb_list):
    comb_sum = 0
    for val in comb_list:
        comb_sum += nCk(val[0],val[1])
    return comb_sum
    

diff_list = []
current_num = 0
max_diff = -1
for a in An:
    diff = a - current_num
    if diff == 0:
        print(0)
        exit(0)
    diff_list.append(diff)
    current_num = a +1
diff = N+1 - current_num
diff_list.append(diff)
#print(diff_list)


all_sum = 1
for idx,diff in enumerate(diff_list):
    
    if idx == 0 or len(diff_list):
        diff -= 1
    '''
    if diff == 0:
        all_sum *= 1
    else:
        internal_comb_list = one_two_comb(diff)
        comb_count = sum_comb(internal_comb_list) + 1
        if all_sum > 10**9+7:
            all_sum = all_sum%(10**9+7)
        all_sum *= comb_count
    '''

    comb_count = feruma_list[diff]
    if all_sum > 10**9+7:
        all_sum = all_sum%(10**9+7)
    all_sum *= comb_count

print(all_sum%(10**9+7))


