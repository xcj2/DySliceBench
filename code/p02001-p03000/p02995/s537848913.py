def code_for_A(test=None):

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


def code_for_B(test=None):

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


def code_for_C(test=None):

    if test:
        A, B, C, D = test
    else:
        A, B, C, D = map(int, input().split())

    def divisible_num(A, B, num):
        result = B // num - (A-1) // num
        return result

    n_C_can_devide = divisible_num(A, B, C)
    n_D_can_devide = divisible_num(A, B, D)

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    lcm = int(C * D / gcd(C, D))

    n_CD_can_devide = divisible_num(A, B, lcm)

    print(B - A + 1 - n_C_can_devide - n_D_can_devide + n_CD_can_devide)


def main():
    code_for_C()


if __name__ == '__main__':
    main()
