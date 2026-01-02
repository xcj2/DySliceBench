def low_left(ls,key):
    left,right = -1,len(ls)
    while right - left > 1:
        mid = (right+left)//2
        if ls[mid] >= key:
            right = mid
        else:
            left = mid
    return left+1


def high_right(ls,key):
    left,right = -1,len(ls)
    while right - left > 1:
        mid = (right+left)//2
        if ls[mid]<=key:
            left = mid
        else:
            right = mid
    return right


def test():
    n = int(input())
    A,B,C = [list(sorted((map(int,input().split())))) for i in range(3)]
    ans = 0

    for b in B:
        ans += (n-high_right(C,b))*low_left(A,b)
    print(ans)


if __name__ == "__main__":
    test()
