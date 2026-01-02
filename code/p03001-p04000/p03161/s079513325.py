# python3
import sys

input = sys.stdin.readline


def main():
    # 2 <= N <= pow(10,5), 1 <= K <= 100
    N, K = [int(ele) for ele in input().split()]
    h = [Node(int(ele)) for ele in input().split()]

    for idx, n in enumerate(h):
        s = max(0, idx - K)
        n.parents = h[s:idx]
        n.cal_dp()

    print(h[-1].dp_val)


class Node():

    def __init__(self, val):
        self.val = val
        self.dp_val = 1000000000000
        self.parents = []

    def cal_dp(self):
        if self.parents == []:
            self.dp_val = 0
            return

        for n in self.parents:
            self.dp_val = min(self.dp_val, abs(n.val - self.val)+n.dp_val)


if __name__ == '__main__':
    main()
