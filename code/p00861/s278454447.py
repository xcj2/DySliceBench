import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

def main():
    rr = []

    def f(n):
        _a = [n]
        while 1:
            s = S()
            if s == '.':
                break
            _a.append(s)
        _ks = {}
        _d = {}
        for _i in range(len(_a)):
            _s = _a[_i]
            if '=' in _s:
                try:
                    exec(_s,_d)
                    for _k in _ks.keys():
                        # print('_k',_k)
                        _kl = _d[_k].keys()
                        # print('_kl',_kl)
                        if _kl and max(_kl) >= _ks[_k]:
                            # print('mk', _s, _k,_kl)
                            return _i + 1
                except:
                    # print('except', _s)
                    # print('_d',_d.keys(),_d['z'])
                    return _i + 1
            else:
                _k = _s.split('[')[0]
                _n = int(_s.split('[')[1].split(']')[0])
                _ks[_k] = _n
                # print('tg', _k + ' = {}', _n)
                if _n < 1:
                    continue
                exec(_k+"={}",_d)
        return 0

    while 1:
        n = S()
        if n == '.':
            break
        rr.append(f(n))

    return '\n'.join(map(str,rr))


print(main())

