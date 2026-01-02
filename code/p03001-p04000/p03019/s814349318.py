import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def II(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def SI(): return input()
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')

from bisect import bisect_right, bisect_left

def main():
    N, X = LI()
    b_l_u = []
    for i in range(N):
        b_l_u.append(LI())

    sum_of_test = [ (b_l_u_i[1]*b_l_u_i[0]+b_l_u_i[2]*(X-b_l_u_i[0]), i) for i,b_l_u_i in enumerate(b_l_u)]
    sum_of_test.sort(reverse=True)  # O(nlogn)

    cumsum_of_test = []
    tmp = 0
    for i in sum_of_test:  # O(n)
        tmp += i[0]
        cumsum_of_test.append(tmp)

    B = sum([l*b for b, l, u in b_l_u])  # O(n)
    head = bisect_right(cumsum_of_test, B)-1
    cumsum = cumsum_of_test[head]


    take_li = []
    for j, (sum_, i) in enumerate(sum_of_test):  # O(N)
        # cumsum の中に入っていたら、引く。
        if j <= head:
            new_head = bisect_right(cumsum_of_test, B+sum_)-1  # O(log N)
            new_cumsum = cumsum_of_test[new_head] - sum_
            left = B - new_cumsum
            take_1 = X * new_head
        else:
            left = B - cumsum
            take_1 = X*(head+1)

        if head==-1:  # i番目を下からとっていくコードのみでOK.
            left = B
            take_1 = 0

        b, l, u = b_l_u[i]
        from math import ceil
        if left/l <= b:
            take = ceil(left/l)
        else:
            take = b + ceil((left - b*l)/u)

        if take > X: continue

        take_li.append(take+take_1)

    print(min(take_li))

main()