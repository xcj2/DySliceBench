def binary_search_a(n, a, k):
    #a_i < kを満たすa_iの個数を返す関数

    lb = 0
    ub = n - 1

    if a[ub] < k:
        return n
    elif a[lb] >= k:
        return 0

    while (ub - lb > 1):
        mid = int((ub + lb) / 2)
        if a[mid] < k:
            lb = mid
        elif a[mid] >= k:
            ub = mid
    
    return lb + 1

def binary_search_c(n, c, k):
    #c_i > kを満たすc_iの個数を返す関数

    lb = 0
    ub = n - 1

    if c[ub] <= k:
        return 0
    elif c[lb] > k:
        return n

    while (ub - lb > 1):
        mid = int((ub + lb) / 2)
        if c[mid] > k:
            ub = mid
        elif c[mid] <= k:
            lb = mid
    
    return n - ub
        

def answer(n, a, b, c):
    ans = 0

    a.sort()
    c.sort()
    #bはソートしなくてもよい

    for k in b:
        ans += binary_search_a(n, a, k) * binary_search_c(n, c, k)
        #print(binary_search_a(n, a, k),binary_search_c(n, c, k))
    return ans


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

print(str(answer(n, a, b, c)))