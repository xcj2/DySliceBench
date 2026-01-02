import bisect

def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))
    a.append(0)
    ans = solve(a, n)
    print(ans)

def solve(a, n):
    if not check(a, n):
        return -1

    base = 0
    s = 0
    for i in range(n):
        if a[i] > base + i:
            return -1
        
        if a[i + 1] <= a[i]:
            s += a[i]
        
        base = i - a[i]
    
    return s

def check(a, n):
    if a[0] != 0:
        return False
    
    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            return False

    return True

main()