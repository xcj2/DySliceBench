class Dice:

    def __init__(self):
        # 初期値がない場合
        self.t = 1
        self.s = 2
        self.e = 4
        self.w = 8
        self.n = 16
        self.b = 32

    def __init__(self, t, s, e, w, n, b):
        # 初期値が指定される場合
        self.t = t
        self.s = s
        self.e = e
        self.w = w
        self.n = n
        self.b = b

    def rot(self, way):
        if way == "S":
            self.t, self.s, self.e, self.w, self.n, self.b = self.n, self.t, self.e, self.w, self.b, self.s
        elif way == "N":
            self.t, self.s, self.e, self.w, self.n, self.b = self.s, self.b, self.e, self.w, self.t, self.n
        elif way == "E":
            self.t, self.s, self.e, self.w, self.n, self.b = self.w, self.s, self.t, self.b, self.n, self.e
        elif way == "W":
            self.t, self.s, self.e, self.w, self.n, self.b = self.e, self.s, self.b, self.t, self.n, self.w
        
        
def main():

    t,s,e,w,n,b = map(int, input().split())
    cmd = input().upper()
    dice1 = Dice(t,s,e,w,n,b)

    for i in range(len(cmd)):
        dice1.rot(cmd[i])
    
    print(dice1.t)

if __name__ == '__main__':
    main()


