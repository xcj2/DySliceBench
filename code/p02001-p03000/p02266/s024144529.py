def print_puddle(puddle):
    n = len(puddle)
    if n > 0:
        print(n, end=' ')
    else:
        print(n)
    for i in range(n):
        if i != n - 1:
            print(puddle[i][1], end=' ')
        else:
            print(puddle[i][1])



def solve(A):
    left = []
    puddle = []
    sum_all = 0
    for i, a in enumerate(A):
        if a == '\\':
            left.append(i)
        elif a == '/' and len(left) > 0:
            left_i = left.pop()
            a = i - left_i
            sum_paddle = i - left_i
            sum_all += a
            while len(puddle) and puddle[-1][0] > left_i:
                tmp = puddle.pop()
                sum_paddle += tmp[1]

            puddle.append((left_i, sum_paddle))
    print(sum_all)
    print_puddle(puddle)


def main():
    A = list(input())

    solve(A)


if __name__ == "__main__":
    main()

