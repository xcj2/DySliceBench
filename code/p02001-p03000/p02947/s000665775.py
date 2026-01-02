#!/usr/bin/env python3
import sys
import math
def combinations_count(n, r):
    if n<r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def solve(N: int, s: "List[str]"):
    s_dict = {}    
    for i in range(N):
        ss = ''.join(sorted(list(s[i])))
        if s_dict.get(ss) == None:
            s_dict[ss] = 1
        else:
            s_dict[ss] += 1
    answer = 0
    for _,value in s_dict.items():
        answer += combinations_count(value,2)


    print(answer)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, s)

if __name__ == '__main__':
    main()
