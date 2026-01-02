def main():
    from sys import stdin
    def input():
        return stdin.readline().strip()

    # return max({i | i*i < a*b})
    # binary search
    def square_range(a, b):
        left = a
        right = b - 1
        while left < right:
            center = (left + right + 1) // 2
            if center * center < a * b:
                left = center
            else:
                right = center - 1
        return left

    q = int(input())
    ans = [0] * q

    for lap in range(q):
        a, b = map(int, input().split())

        if a < b:
            mid = square_range(a, b)
        else:
            mid = square_range(b, a)

        if mid * (mid + 1) < a * b:
            ans[lap] = (2 * mid - 1)
        else:
            ans[lap] = (2 * mid - 2)
    
    for i in ans:
        print(i)

main()