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

h,w = li()

# タテに3つ
if w%3 == 0:
    pat1 = 0
else:
    pat1 = h

# ヨコに3つ
if h%3 == 0:
    pat2 = 0
else:    
    pat2 = w

# T形に分ける
h1to = h//3
h2to = h-h1to

wto = w//2

choco1 = h1to * w
choco2 = h2to*wto
choco3 = h2to*(w-wto)

pat3 = max(choco1,choco2,choco3) - min(choco1,choco2,choco3)

h1to = h//3+1
h2to = h-h1to

wto = w//2

choco1 = h1to * w
choco2 = h2to*wto
choco3 = h2to*(w-wto)

pat4 = max(choco1,choco2,choco3) - min(choco1,choco2,choco3)


# ト型に分ける
w1t = w//3
w2t = w - w1t

ht = h//2

choco1 = w1t * h
choco2 = w2t * ht
choco3 = w2t * (h-ht)

pat5 = max(choco1,choco2,choco3) - min(choco1,choco2,choco3)


w1t = w//3+1
w2t = w - w1t

ht = h//2

choco1 = w1t * h
choco2 = w2t * ht
choco3 = w2t * (h-ht)

pat6 = max(choco1,choco2,choco3) - min(choco1,choco2,choco3)

print(min(pat1,pat2,pat3,pat4,pat5,pat6))