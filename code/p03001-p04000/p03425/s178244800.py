import itertools
def MI(): return map(int, input().split())
def II(): return int(input())
def IS(): return input()
def LI(): return list(map(int, input().split()))


n = II()
s = [IS()[0] for _ in range(n)]
m = s.count('M');
a = s.count('A');
r = s.count('R');
c = s.count('C');
h = s.count('H');

march = ['M','A','R','C','H']
ans = 0
for combination in list(itertools.combinations(march, 3)):
    count = 1
    for char in combination:
        if char == 'M':
            count *= m
        elif char == 'A':
            count *= a
        elif char == 'R':
            count *= r
        elif char == 'C':
            count *= c
        else:  # char == 'h'
            count *= h
    ans += count
print(ans)
