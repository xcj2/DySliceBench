import math

tr = []

def check(n, k, P):
    i = 0
    for j in range(k):
        s = 0
        while s + tr[i] <= P:
            s += tr[i]
            i += 1
            if i == n:
                return n
    return i

def solve(n, k):
    left = 0
    right = 100000 * 100000
    while right - left > 1:
        mid = math.floor((left+right) / 2)
        v = check(n, k, mid)
        if v >= n:
            right = mid
        else:
            left = mid
    return right

def main():
    input_line = input().split(" ")
    n = int(input_line[0])
    k = int(input_line[1])
    
    for _ in range(n):
        w = int(input())
        tr.append(w)

    ans = solve(n, k)
    
    print(ans)

if __name__ == '__main__':
    main()
