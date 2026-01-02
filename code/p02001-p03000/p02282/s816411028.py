from collections import deque


class Node:
    def __init__(self, parent=-1, left=-1, right=-1):
        self.parent = parent
        self.left = left
        self.right = right


n = int(input())
pre_lst = deque(map(int, input().split()))
in_lst = list(map(int, input().split()))
post_lst = []


def reconstruction(l, r):
    if l >= r:
        return

    c = pre_lst.popleft()
    m = in_lst.index(c)

    reconstruction(l, m)
    reconstruction(m+1, r)

    post_lst.append(c)
    return


def main():
    reconstruction(0, n)
    print(" ".join([str(i) for i in post_lst]))


if __name__ == '__main__':
    main()

