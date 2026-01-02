import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop

#------------------------------------------#

BIG_NUM = 2000000000
HUGE_NUM = 9999999999999999
MOD = 1000000007
EPS = 0.000000001


def MIN(A,B):
    if A <= B:
        return A
    else:
        return B

def MAX(A,B):
    if A >= B:
        return A
    else:
        return B

#------------------------------------------#

class Point:
    def __init__(self,arg_x,arg_y):
        self.x = arg_x
        self.y = arg_y


def roll(div1,div2):
    tmp_start = Point(div2.x-div1.x,div2.y-div1.y)
    tmp_end = Point(tmp_start.x*math.cos(math.pi/3) -tmp_start.y*math.sin(math.pi/3),
                    tmp_start.x*math.sin(math.pi/3) + tmp_start.y*math.cos(math.pi/3))
    ret = Point(tmp_end.x + div1.x,tmp_end.y + div1.y)
    return ret;


def outPut(point):
    print("%.8f %.8f"%(point.x,point.y))


def calc(left,right,count):
    div1 = Point((2*left.x + right.x)/3,(2*left.y + right.y)/3)
    div2 = Point((2*right.x + left.x)/3,(2*right.y + left.y)/3)
    peek = roll(div1,div2)

    if count > 1:
        calc(left,div1,count-1)
        calc(div1,peek,count-1)
        calc(peek,div2,count-1)
        calc(div2,right,count-1)
    else:
        outPut(left);
        outPut(div1);
        outPut(peek);
        outPut(div2);


N = int(input())
left = Point(0,0)
right = Point(100,0)

if N == 0:
    outPut(left)
    outPut(right)
else:
    calc(left,right,N)
    outPut(right)


