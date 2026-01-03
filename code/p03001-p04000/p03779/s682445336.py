

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    X+i+(i+1)+(i+2)+..
    
    X < n*(n+1)//2

    n*(n+1)//2-(n-1)*n//2 > n ?
    n//2(2) > n ? false
    """
    X = read_int()
    if X == 1:
        return 1
    low, high = 1, 10**9
    while high-low > 1:
        mid = low+(high-low)//2
        if mid*(mid+1)//2 >= X:
            high = mid
        else:
            low = mid
    if high*(high+1)//2 == X:
        return high
    return high


if __name__ == '__main__':
    print(solve())
