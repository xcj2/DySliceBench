def test():
    n = int(input())
    A,B,C = [list(sorted(map(int,input().split()))) for i in range(3)]
    ans = 0

    for b in B:
        ans += low_left(A,b) * (n-high_right(C,b))
    print(ans) 


def low_left(ls,t):
    low,high = 0,len(ls)
    while low<high:
        mid = (low+high)//2
        if ls[mid] < t:
            low = mid + 1
        else:
            high = mid
    return low


def high_right(ls,t):
    low,high = 0,len(ls)
    while low<high:
        mid = (low+high)//2
        if ls[mid] > t:
            high = mid
        else:
            low = mid + 1
    return low


if __name__ == "__main__":
    test()
