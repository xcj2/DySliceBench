import sys
sys.setrecursionlimit(10 ** 5)
lst = [[1,2], [2, 5], [3, 5], [4, 4], [5, 5], [6, 6], [7, 3], [8, 7], [9, 6]]
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse = True)
# print (A)

def num(k):
    return lst[k-1][1]

# for i in A:
    # print (num(i), end = ', ')
# print ()

INF = 10 ** 5
dp_lst = [-INF] * (N + 1)
dp_lst[0] = 0
def dp(i):
    if dp_lst[i] != -INF:
        return dp_lst[i]
    tmp = -INF
    for j in A:
        if i >= num(j):
            tmp = max(tmp, dp(i - num(j)) + 1)
    dp_lst[i] = tmp
    return dp_lst[i]

a = dp(N)
# print (a)
# print (dp_lst)   
# print ([0] * 10 +[i+1 for i in range(20)])

# print (len(str(71111111111111111111111111111111111111111111111111)))

def check(A):
    if N - num(A) < 0:
        return False
    if dp_lst[N-num(A)] == dp_lst[N] - 1:
        return True
    else:
        return False

# print (a)
while a > 0:
    for i in A:
        if check(i):
            print (i, end = '')
            N -= num(i)
            a -= 1
            break
        else:
            pass
            # print ('B')
print ()