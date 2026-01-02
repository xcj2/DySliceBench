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



def solve(N: int, S: "List[str]"):
    counter = Counter()
    for s in S:
        counter.add(s)
    
    print(len(counter.get_dict().keys()))
        
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)



if __name__ == "__main__":
    main()
