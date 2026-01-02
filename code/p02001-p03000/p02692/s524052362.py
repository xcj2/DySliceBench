# -*- coding: utf-8 -*-
import sys

buff_readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

def read_int_n():
    return list(map(int, buff_readline().split()))


def read_str():
    return readline().strip()


def slv(N, A, B, C, S):
    D = [A, B, C]
    ans = []

    def f(s):
        t = []
        if 'A' in s:
            t.append(0)
        if 'B' in s:
            t.append(1)
        if 'C' in s:
            t.append(2)
        return t
    for i, s in enumerate(S):
        t = f(s)
        if D[t[0]] == 0 and D[t[1]] == 0:
            print('No')
            return
        else:
            if D[t[0]] == D[t[1]] == 1 and i != N-1:
                ns = S[i+1]
                if s == ns:
                    ans.append(t[1])
                    D[t[0]] -= 1
                    D[t[1]] += 1
                else:
                    n = set(t) & set(f(ns))
                    m = set(t) - n
                    n = n.pop()
                    m = m.pop()
                    ans.append(n)
                    D[n] += 1
                    D[m] -= 1


            elif D[t[0]] > D[t[1]]:
                ans.append(t[1])
                D[t[0]] -= 1
                D[t[1]] += 1
            else:
                ans.append(t[0])
                D[t[0]] += 1
                D[t[1]] -= 1

    print('Yes')
    for a in ans:
        if a == 0:
            print('A')
        elif a == 1:
            print('B')
        else:
            print('C')



def main():
    N, A, B, C = read_int_n()
    S = [read_str() for _ in range(N)]
    (slv(N, A, B, C, S))

if __name__ == '__main__':
    main()
