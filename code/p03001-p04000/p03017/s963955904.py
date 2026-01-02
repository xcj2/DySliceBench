import sys
INPUT = sys.stdin.readline

def SINGLE_INT(): return int(INPUT())
def MULTIPLE_INT_LIST(): return list(map(int, INPUT().split()))
def MULTIPLE_INT_MAP(): return map(int, INPUT().split())
def SINGLE_STRING(): return INPUT()
def MULTIPLE_STRING(): return INPUT().split()

N, A, B , A_goal, B_goal = MULTIPLE_INT_MAP()
S = SINGLE_STRING()

def surpass():

    if '...' in S[B-2:B_goal+1]:
        return 'Yes'
    else:
        return 'No'


if '##' in S[A-1: A_goal+1] or '##' in S[B-1:B_goal+1]:
    print('No')

else:
    if A_goal < B_goal:
        print('Yes')
    else:
        print(surpass())