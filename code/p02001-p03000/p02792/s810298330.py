def calc(left, right, N):
    def left_match(x):
        return int(str(x)[0]) == left
    def right_match(x):
        return x % 10 == right
    cnt = 0
    n = 1
    while n <= N:
        if not left_match(n):
            length = len(str(n))
            n += 10**(length - 1)
        elif not right_match(n):
            n += 1
        else:
            cnt += 1
            n += 1
    return cnt


def main():
    N = int(input())
    counter = dict()
    for left in range(1, 10):
        for right in range(1, 10):
            counter[(left, right)] = calc(left, right, N)
    answer = 0
    for left in range(1, 10):
        for right in range(1, 10):
            answer += counter[(left, right)] * counter[(right, left)]
    print(answer)


if __name__ == '__main__':
    main()