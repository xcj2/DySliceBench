import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    N = in_n()
    A = in_nl()

    def sad(x):
        s = 0
        for i in range(N):
            s += abs(A[i] - (x + i + 1))
        return s

    def binary_search(min_n, max_n):

        while max_n - min_n != 1:
            tn = (min_n + max_n) // 2
            if sad(tn) < sad(tn + 1):
                max_n = tn
            else:
                min_n = tn

        return max_n

    b = binary_search(min(A) - 10**9, max(A) + 10**9)
    print(sad(b))


if __name__ == '__main__':
    main()
