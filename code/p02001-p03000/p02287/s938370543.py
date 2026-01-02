MAX = 100000


def parent(i):
    return i//2


def left(i):
    return 2*i


def right(i):
    return 2*i+1


def main():
    global H
    H = int(input())
    A = [0] * (MAX+1)

    v_s = input().split(' ')

    for i in range(H):
        A[i+1] = int(v_s[i])

    for i in range(1, H+1):
        s = 'node {}: key = {},'.format(i, A[i])
        if parent(i) >= 1:
            s += ' parent key = {},'.format(A[parent(i)])
        if left(i) <= H:
            s += ' left key = {},'.format(A[left(i)])
        if right(i) <= H:
            s += ' right key = {},'.format(A[right(i)])
        print(s + ' ')


if __name__ == '__main__':
    main()

