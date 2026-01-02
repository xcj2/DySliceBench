# python3


def main():
    N = input()
    h = [Node(int(ele)) for ele in input().split()]
    cal_dp(h)
    print(h[-1].dp_val)


def cal_dp(h):
    for idx, n in enumerate(h):
        if idx == 0:
            n.dp_val = 0

        elif idx == 1:
            n.dp_val = abs(h[0].val - n.val)
        else:
            n.dp_val = min(h[idx-1].dp_val + abs(n.val - h[idx-1].val),
                           h[idx-2].dp_val + abs(n.val - h[idx-2].val))


class Node():

    def __init__(self, val):
        self.val = val
        self.dp_val = 'unk'


if __name__ == '__main__':
    main()
