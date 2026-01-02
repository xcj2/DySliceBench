import sys
INPUT = sys.stdin.readline

def SINGLE_INT(): return int(INPUT())
def MULTIPLE_INT_LIST(): return list(map(int, INPUT().split()))
def MULTIPLE_INT_MAP(): return map(int, INPUT().split())
def SINGLE_FLOAT(): return float(INPUT())
def MULTIPLE_FLOAT_LIST(): return list(map(float, INPUT().split()))
def MULTIPLE_FLOAT_MAP(): return map(float, INPUT().split())
def SINGLE_STRING(): return INPUT()
def MULTIPLE_STRING(): return INPUT().split()

N = SINGLE_INT()

ratings = []

for i in range(N):
    c, s = MULTIPLE_STRING()
    s_int = int(s)

    ratings.append((c, s_int, i+1))

ratings.sort(key=lambda x: x[1], reverse=True)
ratings.sort(key=lambda x: x[0])

for c, s_int, id in ratings:
    print(id)