def get_lmb(N):
    while (N >= 10):
        N = int(N/10)
    return N

def get_rmb(N):
    return N%10

def find_all():
    from collections import defaultdict
    dic = defaultdict(int)
    N = int(input())
    for i in range(1, N+1):
        lmb, rmb = get_lmb(i), get_rmb(i)
        dic[(lmb, rmb)] += 1
    # print(dic)
    count = 0
    for i in range(1, 10):
        for j in range(1, 10):
            count += dic[(i, j)] * dic[(j, i)]
    # for i in range(1, 10):
    #     count += dic[(i, i)] * dic[(i, i)]
    return count

print(find_all())