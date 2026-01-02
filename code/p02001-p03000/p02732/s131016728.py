def main():
    import math
    import collections
    N = int(input())
    A = list(map(int, input().split()))
    tt = 0
    #ans = list()
    ann = 0

    def comb(m, n):
        #return math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
        return ((m - 1 + 1) / 1) * (m - 2 + 1) / 2

    '''
    def A_count(n):
        if n in memo:
            return memo[n]
        h = A.count(i)
        memo[n] = A.count(i)
        return h
    '''

    C = collections.Counter(A)
    for i in C.values():
        if i>=2:
            tt = tt + comb(i, 2)

    for i in A:
        f = C[i] #A_count(A[i])
        if f>=3:
            ann = (tt - comb(f, 2) + comb(f-1, 2))
        elif f==2:
            ann = tt - comb(f, 2)
        else:
            ann = tt
        print(int(ann))

    #for i in ans:
    #    print(i)


if __name__ == '__main__':
    main()