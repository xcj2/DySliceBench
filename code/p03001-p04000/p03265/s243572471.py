# 入力
import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())

x1, y1, x2, y2 = li()

mean = (abs(x2-x1) + abs(y2-y1)) / 2
cent_x, cent_y = 0,0

if x1 >= x2 and y2 >= y1:
    cent_x, cent_y = x1-mean, y2-mean
    
elif x1 >= x2 and y1 >= y2:
    cent_x, cent_y = x2+mean, y1-mean
    
elif x2 >= x1 and y1 >= y2:
    cent_x, cent_y = x1+mean, y2+mean
    
else:
    cent_x, cent_y = x2-mean, y1+mean
    
x2_v, y2_v = x2-cent_x, y2-cent_y

x3_v, y3_v = -y2_v, x2_v 
x4_v, y4_v = -y3_v, x3_v

x3, y3 = int(x3_v+cent_x), int(y3_v+cent_y)
x4, y4 = int(x4_v+cent_x), int(y4_v+cent_y)

print(x3,y3,x4,y4)