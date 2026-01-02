import sys
import heapq


def main():
    n, k = [int(s) for s in sys.stdin.readline().strip().split()]
    a = [int(s) for s in sys.stdin.readline().strip().split()]
    f = [int(s) for s in sys.stdin.readline().strip().split()]
    # n, k = 3, 5
    # a = [4, 2,1]
    # f = [2, 3, 1]

    a.sort(reverse=True)
    f.sort()

    def possible(x1):
        improved = 0
        for i in range(n):
            before = a[i] * f[i]
            if before > x1:
                needed_to_be_reduced = before - x1
                if needed_to_be_reduced % f[i] == 0:
                    plus_one = 0
                else:
                    plus_one = 1
                improved += (needed_to_be_reduced // f[i]) + plus_one
                if improved > k:
                    return False
        return True

    def b_search():
        lo = 0
        hi = 10 ** 12
        # (lo, hi]
        # hi is always possible
        # lo might be possible

        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid+1
        return hi

    ans = b_search()
    print(ans)


main()

