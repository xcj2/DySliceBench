class fenwick_tree():
    def __init__(self, n:int):
        self.__n = n
        self.__data = [0] * self.__n

    def add(self, p:int, x:int):
        assert (0 <= p) & (p < self.__n)
        p+=1
        while( p<= self.__n):
            self.__data[p-1] += x
            p += p & -p

    def sum(self, l:int, r:int):
        assert (0 <= l) & (l <= r) & (r <= self.__n)
        return self.__sum_mod0(r) - self.__sum_mod0(l)

    def __sum_mod0(self, r:int):
        s = 0
        while(r > 0):
            s += self.__data[r-1]
            r -= r & -r
        return s


import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,q = map(int,readline().split())
a = list(map(int,readline().split()))
query = list(map(int,read().split()))

ft = fenwick_tree(n)
ans = []

for i,ai in enumerate(a):
    ft.add(i,ai)

i = 0
for _ in range(q):
    if(query[i]==0):
        p,x = query[i+1:i+3]
        ft.add(p,x)
    else:
        l,r = query[i+1:i+3]
        ans.append(ft.sum(l,r))
    i += 3

print('\n'.join(map(str,ans)))
