#! /usr/bin/env python3
import sys
sys.setrecursionlimit(10**9)


INF=10**20
class Counter:
    def __init__(self):
        self.dict = {}

    def add(self,x):
        if x in self.dict: self.dict[x] += 1
        else: self.dict[x] = 1

    def decrement(self,x):
        self.dict[x] -= 1
        if self.dict[x] <= 0:
            del self.dict[x]

    def get_dict(self):
        return self.dict


def solve(S):
    N = len(S)

    v1 = [0] * (N+1)
    v1[0] = 0

    for i in range(N):
        v1[i+1] = v1[i] * 10 + int(S[i])
        v1[i+1] %= 2019

    counter = Counter()
    for i in range(N+1):
        u = v1[i] * pow(10,201900-i,2019) % 2019
        counter.add(u)

    
    ans = 0
    # print(counter.get_dict())
    for _,count in counter.get_dict().items():
        ans += count * (count-1) // 2
    
    print(ans)

    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = list((next(tokens)))  # type: int
    solve(S)



if __name__ == "__main__":
    main()
