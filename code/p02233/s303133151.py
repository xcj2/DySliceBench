import time
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


# 何も考えずに書いてみたやつ これ一番早いじゃん・・・
def fib_org(n):
    if n in (0, 1):
        return 1

    count = 3
    prevprev = 1
    prev = 2
    while count <= n:
        tmp = prevprev + prev
        prevprev = prev
        prev = tmp
        count += 1

    return prev


# 教科書通りの再起のfib
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)

# def fib2(n):
#     if n == 0 or n == 1:
#         return 1
#     if
#     return fib(n - 2) + fib(n - 1)


N = int(input())
F = [0 for i in range(N + 1)]


def fib_memo(n):
    if n == 0 or n == 1:
        F[n] = 1
    if F[n] != 0:
        return F[n]
    F[n] = fib_memo(n - 2) + fib_memo(n - 1)
    return F[n]


# start = time.time()
# print('case1: original fib calculator')
# print('result:{}'.format(fib_org(N)))
# elapsed_time = time.time() - start
# print("elapsed_time:{0}[sec]".format(elapsed_time))

# start = time.time()
# print('case2: base fib calculator')
# print('result:{}'.format(fib(N)))
# elapsed_time = time.time() - start
# print("elapsed_time:{0}[sec]".format(elapsed_time))

# start = time.time()
# print('case3: memo fib calculator')
# print('result:{}'.format(fib_memo(N)))
# elapsed_time = time.time() - start
# print("elapsed_time:{0}[sec]".format(elapsed_time))

# 以下提出用
print(fib_org(N))

