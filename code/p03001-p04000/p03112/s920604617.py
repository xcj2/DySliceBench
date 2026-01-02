import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools


sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    A, B, Q = LI()
    s, t, x = [], [], []
    [s.append(I()) for i in range(A)]
    [t.append(I()) for i in range(B)]
    [x.append(I()) for i in range(Q)]
    s = [-10**18] + s + [10**18]
    t = [-10**18] + t + [10**18]

    #  print(A, B,Q,s,t,x)
    #  A = 10**5
    #  B = 10 ** 5
    #  Q = 10**5
    #  [s.append(i) for i in range(A)]
    #  [t.append(i) for i in range(B)]
    #  [x.append(i) for i in range(Q)]
    #  s = [-10**18] + s + [10**18]
    #  t = [-10**18] + t + [10**18]
    #  print(len(s), len(t), s[0], s[-1])


    for start in x:
        #  first_temple = [temple for temple in t if temple <= start]
        first_temple_idx = bisect.bisect_left(t, start) - 1
        second_temple_idx = first_temple_idx + 1
        temples = [first_temple_idx, second_temple_idx]
        first_shrine_idx = bisect.bisect_left(s, start) - 1
        second_shrine_idx = first_shrine_idx + 1
        shrines = [first_shrine_idx, second_shrine_idx]
        #  print(temples, shrines)

        #  if len(first_temple) != 0:
        #      first_temple = first_temple[-1:]
        #  second_temple = [temple for temple in t if temple > start]
        #  if len(second_temple) != 0:
        #      second_temple = second_temple[:1]
        #  temples = first_temple + second_temple
        #  #  print('temples', temples)

        #  first_shrine = [sh for sh in s if sh <= start]
        #  if len(first_shrine) != 0:
        #      first_shrine = first_shrine[-1:]
        #  second_shrine = [sh for sh in s if sh > start]
        #  if len(second_shrine) != 0:
        #      second_shrine = second_shrine[:1]
        #  shrines = first_shrine + second_shrine
        #  print('shrines', shrines)

        result = 10**11
        for temple in temples:
            for shrine in shrines:
                #  print('temple/shrine', temple, shrine)
                #  print(temple, shrine)
                near = min(abs(start - t[temple]), abs(start - s[shrine]))
                far = max(abs(start - t[temple]), abs(start - s[shrine]))
                if (t[temple] < start and s[shrine] < start) or (t[temple] > start and s[shrine] > start):
                    result = min(result, far)
                elif (t[temple] < start and s[shrine] > start) or (t[temple] > start and s[shrine] < start):
                    result = min(result, near * 2 + far)
                #  print('on-going result', result)

        #  print('result', result)
        print(result)
if __name__ == "__main__":
    main()
