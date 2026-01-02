import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

a,b,c,d,e,f = li()

water_set = set()
sugar_set = set()

MAX = 3000

# ありうる水と砂糖の重さ
for ai in range(0,MAX//100+1,a):
    for bi in range(0,MAX//100+1,b):
        if 100 * (ai + bi) <= MAX:
            water_set.add(100 * (ai + bi))

water_list = sorted(list(water_set))

for ci in range(0,30*e+1,c):
    for di in range(0,30*e+1,d):
        if ci + di <= 30*e:
            sugar_set.add(ci+di)
            
sugar_list = sorted(list(sugar_set))

node_max = -1
sw = 0
sg = 0

for wi in water_list:
    for si in sugar_list:
        if wi+si <= f and si <= e * (wi//100) and wi+si > 0:
            node = (100*si) / (wi+si)
            if node > node_max:
                sw = si + wi
                sg = si
                node_max = node
                
print(sw,sg)