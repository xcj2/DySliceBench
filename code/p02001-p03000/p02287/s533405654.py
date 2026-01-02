import sys
input = sys.stdin.readline
H = int(input())
h = [int(ele) for ele in input().split()]
h = [0] + h


def main():
    for i in range(1, H+1):
        print('node ' + str(i) + ': key = ' +
              str(h[i]) + ', ' + parent(i) + left(i) + right(i))


def parent(i):
    if i == 1:
        return ''

    p_idx = int(i/2)
    return 'parent key = ' + str(h[p_idx]) + ', '


def left(i):
    l_idx = 2*i
    if H < l_idx:
        return ''

    return 'left key = ' + str(h[l_idx]) + ', '


def right(i):
    r_idx = 2*i + 1
    if H < r_idx:
        return ''

    return 'right key = ' + str(h[r_idx]) + ', '


if __name__ == "__main__":
    main()

