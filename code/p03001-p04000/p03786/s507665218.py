import math
def main():
    global N, A
    N = int(input())
    sizes = list(map(int, input().split()))
    A = list(zip(list(range(1, N+1)), sizes))  # color, size
    A.sort(key=lambda x:x[1])
    print(N - binary_search_for_integer(N-1, -1))

def binary_search_for_integer(ok, ng):
    while math.fabs(ok-ng) > 1:
        mid = (ok+ng)//2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok

def solve(x):  # x=index
    if x != 0:
        size = sum([a[1] for a in A[:x]]) + A[x][1]
    else:
        size = A[x][1]

    for i in range(1, N-x):
        if A[x+i][1] <= 2*size:
            size += A[x+i][1] 
        else:
            return False

    return True


if __name__ == "__main__":
    main()
