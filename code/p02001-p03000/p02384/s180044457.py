class Dice:

    def __init__(self):
        # 初期値がない場合
        # 上, 南、東、西、北、下にそれぞれ1, 2, 3, 4, 5, 6がくる想定
        self.t = 1
        self.s = 2
        self.e = 3
        self.w = 4
        self.n = 5
        self.b = 6
        self.rotway = {"S": 0, "N": 1, "E": 2, "W": 3}

    def __init__(self, t, s, e, w, n, b):
        # 初期値が指定される場合
        self.t = t
        self.s = s
        self.e = e
        self.w = w
        self.n = n
        self.b = b
        self.rotway = {"S": 0, "N": 1, "E": 2, "W": 3}

    def rot(self, way):
        if way == 0:
            self.t, self.s, self.e, self.w, self.n, self.b = self.n, self.t, self.e, self.w, self.b, self.s
        elif way == 1:
            self.t, self.s, self.e, self.w, self.n, self.b = self.s, self.b, self.e, self.w, self.t, self.n
        elif way == 2:
            self.t, self.s, self.e, self.w, self.n, self.b = self.w, self.s, self.t, self.b, self.n, self.e
        elif way == 3:
            self.t, self.s, self.e, self.w, self.n, self.b = self.e, self.s, self.b, self.t, self.n, self.w
        
        
def main():
    import random

    t,s,e,w,n,b = map(int, input().split())
    dice2 = Dice(t,s,e,w,n,b)
    q = int(input())
    for _ in range(q):
        top, front = map(int, input().split())
        while True:
            if dice2.t == top and dice2.s == front:
                break
            else:
                seed = random.randint(0, 3)
                dice2.rot(seed)
        print(dice2.e)



if __name__ == '__main__':
    main()

