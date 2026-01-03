from functools import reduce
MOD = 10**9 + 7
class MyRange(object):
    def __init__(self, l, r): 
        self.l = l
        self.r = r

    def __and__(self, other):
        return MyRange(max(self.l, other.l), min(self.r, other.r))

    def __len__(self):
        return self.r - self.l

    def __str__(self):
        return "[{}, {})".format(self.l, self.r)

def hoge(arr):
    res = [MyRange(arr[0], arr[0]+1)]
    for pre, cur in zip(arr, arr[1:]):
        if pre < cur:
            res.append(MyRange(cur, cur+1))
        else:
            res.append(MyRange(1, cur+1))
    return res

if __name__ == "__main__":
    N = int(input())
    T = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    B = [t & a for t, a in zip(hoge(T), hoge(A[::-1])[::-1])]
    # print(*B)
    try:
        C = list(map(len, B))
        print(reduce(lambda a, b: (a * b) % MOD, C))
    except ValueError:
        print(0)
