"""
コッホ曲線を構成する
numpyは使えないっぽい
"""
import math

class Point: 
    #こうすると見やすくなるっぽいけどそうするんだったらPoint(,)の形で全部書いていくと良い
    def __init__(self, x, y):
        self.x = x
        self.y = y


def outPut(point):
    print("%.8f %.8f"%(point.x, point.y))

def calc(depth, left, right):
    dif_x = right.x-left.x
    dif_y = right.y-left.y

    nleft_x = left.x+dif_x/3
    nleft_y = left.y+dif_y/3

    nright_x = right.x-dif_x/3
    nright_y = right.y-dif_y/3

    #dif/3を回転させる
    top_x = (dif_x*math.cos(math.pi/3)-dif_y*math.sin(math.pi/3))/3+nleft_x
    top_y = (dif_x*math.sin(math.pi/3)+dif_y*math.cos(math.pi/3))/3+nleft_y

    new_left = Point(nleft_x, nleft_y)
    new_right = Point(nright_x, nright_y)
    tmp_top = Point(top_x, top_y)

    if depth > 1:
        calc(depth-1, left, new_left)
        calc(depth-1, new_left, tmp_top)
        calc(depth-1, tmp_top, new_right)
        calc(depth-1, new_right, right)
    else: #depth==1が停止条件
        outPut(left)
        outPut(new_left)
        outPut(tmp_top)
        outPut(new_right) #rightは抜いてある

n = int(input())
start = Point(0, 0)
end = Point(100, 0)

if n == 0:
    outPut(start)
    outPut(end)
else:
    calc(n, start, end)
    outPut(end)

    
                        



