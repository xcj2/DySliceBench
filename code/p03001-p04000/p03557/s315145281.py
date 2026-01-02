def main():
    n = int(input())
    A,B,C = [sorted(list(map(int,input().split()))) for i in range(3)]
    ans = 0
    for b in B:
        ans += low(A,b)*(n-high(C,b))
    print(ans)


def low(A,key):
    left,right = -1,len(A)
    while right - left > 1:
        mid = (left+right)//2
        if A[mid] >= key:
            right = mid
        else:
            left = mid
    return left+1


def high(C,key):
    left,right = -1,len(C)
    while right - left > 1:
        mid = (left+right)//2
        if C[mid] <= key:
            left = mid
        else:
            right = mid
    return right


if __name__ == "__main__":
    main()
