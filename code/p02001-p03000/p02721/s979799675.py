import sys
sys.setrecursionlimit(100000000)


def main():
    N, K, C = map(int, input().split())
    S = input()

    def forward(k):
        i = 0
        day = 0
        days = [-1] * k
        l = len(S)
        while day < k and i < l:
            while S[i] == 'x':
                i += 1
                if i >= l:
                    return None
            days[day] = i
            day += 1
            i += 1 + C
        if day < k:
            return None
        return days

    def backward(k):
        day = k
        days = [-1] * k
        l = len(S)
        i = l - 1
        while day > 0 and i >= 0:
            while S[i] == 'x':
                i -= 1
                if i < 0:
                    return None
            day -= 1
            days[day] = i
            i -= (1 + C)
        if day > 0:
            return None
        return days

    left = forward(K)
    if left is None:
        return

    right = backward(K)
    for i, j in zip(left, right):
        if i == j:
            print(i + 1)

main()
