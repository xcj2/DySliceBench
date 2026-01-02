# Aizu Problem ITP_1_5_D: Structured Programming
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")

res = []


def CHECK_NUM2(n, i):
    x = i
    if x % 3 == 0:
        res.append(i)
    else:
        while True:
            if x % 10 == 3:
                res.append(i)
                break
            x //= 10
            if x == 0:
                break
    i += 1
    if i <= n:
        CHECK_NUM(n, i)
        
def CHECK_NUM(n, i):
    while True:
        x = i
        if x % 3 == 0:
            res.append(i)
        else:
            while True:
                if x % 10 == 3:
                    res.append(i)
                    break
                x //= 10
                if x == 0:
                    break
        i += 1
        if i > n:
            break
        
def call(n):
    CHECK_NUM(n, 1)
    

n = int(input())
#n=1000
call(n)
print(' ' + ' '.join([str(r) for r in res]))