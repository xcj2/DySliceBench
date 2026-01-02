# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

class Dice():
    
    #      e[4]
    # e[3] e[0] e[2] e[5]
    #      e[1]

    #      m[4]
    # m[3] m[0] m[2]
    #      m[1]
    #      m[5]
    
    def __init__(self, nums):
        self.pos = nums
    
    def rot_E(self):
        e = self.pos
        self.pos = [e[3], e[1], e[0], e[5], e[4], e[2]]

    def rot_W(self):
        e = self.pos
        self.pos = [e[2], e[1], e[5], e[0], e[4], e[3]]

    def rot_S(self):
        e = self.pos
        self.pos = [e[4], e[0], e[2], e[3], e[5], e[1]]

    def rot_N(self):
        e = self.pos
        self.pos = [e[1], e[5], e[2], e[3], e[0], e[4]]
        
    def rot_CW(self):
        e = self.pos
        self.pos = [e[0], e[2], e[4], e[1], e[3], e[5]]

    def rot_CCW(self):
        e = self.pos
        self.pos = [e[0], e[3], e[1], e[4], e[2], e[5]]

    def rot_180(self):
        self.rot_CW()
        self.rot_N()
        self.rot_W()

        
    def top(self):
        return self.pos[0]

    def face(self):
        return self.pos[1]

    def right(self, tf=None):
        # tf = (t,f) : 上面 / 正面のラベル

        if tf == None:
            print(self.pos[2])
            return

        t = self.pos.index(tf[0])  # 上面（の扱いになっている）のラベルを取得
        f = self.pos.index(tf[1])  # 前面（の扱いになっている）のラベルを取得
        
        # u,f,r
        dr = [(1,2,4,3),(0,3,5,2),(0,1,5,4),(0,4,5,1),(0,2,5,3),(1,3,4,2)]
        r = (dr[t].index(f) + 1) % 4
        print(self.pos[dr[t][r]])
        return

    def left(self):
        print(self.pos[3])
        return

    def back(self):
        print(self.pos[4])
        return

    def bottom(self):
        print(self.pos[5])
        return

    def fit_top(self,x):
        if x == 0:
            self.rot_S()
            self.rot_S()
        if x == 1:
            self.rot_N()
        if x == 3:
            self.rot_axis()
            self.rot_axis()
        if x == 4:
            self.rot_S()
        if x == 5:
            self.rot_axis()
            self.rot_axis()
            self.rot_axis()

    def check(self, d):
        f = False
        # 上面からスタート
        
        def rotate4():
            nonlocal f
            for _ in range(4):
                if self.pos == d.pos:
                    f = True
                self.rot_CW()

        rotate4()
        
        d.rot_N()
        rotate4()
        d.rot_S()
        
        d.rot_W()
        rotate4()
        d.rot_E()
        
        d.rot_S()
        rotate4()
        d.rot_N()
        
        d.rot_E()
        rotate4()
        d.rot_W()
        
        d.rot_S()
        d.rot_S()
        rotate4()
        
        return f
    
    
    def position(self, x):
        return self.pos.index(x)
    
# 各方向を総当りでチェックする

# d1 = Dice([int(x) for x in input().split()])
# d2 = Dice([int(x) for x in input().split()])

def main():

    f = False

    n = int(input())
    
    ds = []
    for i in range(n):
        dt = Dice([int(x) for x in input().split()])
        ds.append(dt)
    
        for j in range(i):
            if dt.check(ds[j]):
                f = True

    if f:
        print("No")
    else:
        print("Yes")        

def main2():
    d1 = Dice([6, 2, 4, 3, 5, 1])
    d2 = Dice([6, 5, 4, 3, 2, 1])    
    d3 = Dice([1,2,3,4,5,6])
    print(d1.check(d2))
    print(d1.check(d3))
    print(d2.check(d3))
    
main()
