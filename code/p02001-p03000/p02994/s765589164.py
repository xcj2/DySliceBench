def A(test=None):

    if test:
        pass
    else:
        S = input()

    continuous = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            continuous += 1

    if continuous > 0:
        answer = 'Bad'
    else:
        answer = 'Good'

    print(answer)


def B(test=None):

    if test:
        N, L = test
    else:
        N, L = map(int, input().split())

    _sum = int(L * N - N + N * (N + 1) / 2)

    if L <= 0:
        ate = min(0, L + N - 1)
    else:
        ate = max(0, L)

    print(_sum - ate)

def main():
    # A()
    B()


if __name__ == '__main__':
    main()
