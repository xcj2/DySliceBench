#!/usr/bin/env python3
import sys
import statistics
import collections

def solve(n: int, v: "List[int]"):
    half_length = len(v) // 2
    O = [v[i] for i in range(1, n, 2)]
    E = [v[i] for i in range(0, n, 2)]

    co = list(collections.Counter(O).most_common())
    ce = list(collections.Counter(E).most_common())
    o1 = co[0][0]
    e1 = ce[0][0]

    O_ = list(filter(lambda o: o != o1, O))
    E_ = list(filter(lambda e: e != e1, E))
    num_o_1 = len(O_) 
    num_e_1 = len(E_)

    num = 0
    if e1 != o1:
        num = num_o_1 + num_e_1
    else:
        if len(co) == 1 and len(ce) == 1:
            num = half_length
        elif len(co) == 1:
            e2 = ce[1][0]
            num_e_2 = len(list(filter(lambda e: e != e2, E)))
            num = num_o_1 + num_e_2
        elif len(ce) == 1:
            o2 = co[1][0]
            num_o_2 = len(list(filter(lambda o: o != o2, O)))
            num = num_o_2 + num_e_1
        else:
            e2 = ce[1][0]
            o2 = co[1][0]
            num_e_2 = len(list(filter(lambda e: e != e2, E)))
            num_o_2 = len(list(filter(lambda o: o != o2, O)))
            num = min(num_o_1 + num_e_2, num_o_2 + num_e_1)
    print(num)
    return

def len2(l):
    n = 0
    for i in l:
        n += 1
    return n

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    v = [ int(next(tokens)) for _ in range(n) ]  # type: "List[int]"
    solve(n, v)

if __name__ == '__main__':
    main()
