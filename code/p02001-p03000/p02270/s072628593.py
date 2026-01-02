def allocation(A, k):
    def C(P):
        i = 0
        for j in range(k):
            s = 0  # current load for jth car
            while s + A[i] <= P:
                s += A[i]
                i += 1
                if i == len(A): return True
        return False

    l = 0
    r = 100000*10000  # [0..]
    while l !=r:
        mid = int((l + r) / 2)
        if C(mid):
            r = mid
        else:
            l = mid +1 
    return l

def main():
    N, k = (int(x) for x in input().split())
    A = [int(input()) for i in range(N)]
    print(allocation(A,k))


main()
