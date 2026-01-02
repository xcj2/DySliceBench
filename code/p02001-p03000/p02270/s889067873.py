def binary_search(n, k, lw):
    left = 0
    right = max(lw) * n

    while left <= right:
        mid = (left + right)//2
        if is_underweight(n, k, lw, p=mid):
            right = mid - 1
        else:
            left = mid + 1

    if is_underweight(n, k, lw, p=right):
        return right
    else:
        return left

def is_underweight(n, k, lw, p):
    i = 0
    w = 0
    ck = 1
    while i < n:
        if lw[i] > p:
            return False
        rest = p - w
        if lw[i] <= rest:
            w += lw[i]
            i += 1
        else:
            w = 0
            ck += 1
    return ck <= k

def main():
    n, k = map(int, input().split())
    lw = []
    for _ in range(n):
        lw.append(int(input()))

    p = binary_search(n, k, lw)

    print(p)

if __name__ == '__main__':
    main()

