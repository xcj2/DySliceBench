

class dice:
    def __init__(self,dice):
        self.dice = dice

    def roll_n(self):
        d = self.dice
        self.dice = [d[1],d[5],d[2],d[3],d[0],d[4]]

    def roll_e(self):
        d = self.dice
        self.dice = [d[3],d[1],d[0],d[5],d[4],d[2]]

    def roll_s(self):
        d = self.dice
        self.dice = [d[4],d[0],d[2],d[3],d[5],d[1]]
    
    def roll_w(self):
        d = self.dice
        self.dice = [d[2],d[1],d[5],d[0],d[4],d[3]]

    def top(self):
        return self.dice[0]

    def roll(self,command):
        if command=='N':self.roll_n()
        if command=='E':self.roll_e()
        if command=='S':self.roll_s()
        if command=='W':self.roll_w()

def main():
    com1 = 'SSSWSSS'
    com2 = 'WWWW'
    d = dice(list(map(int,input().split())))
    q = int(input())
    for _ in range(q):
        a,b = map(int,input().split())
        for c in com1:
            if b==d.dice[1]:break
            d.roll(c)
        for c in com2:
            if a==d.dice[0]:print (d.dice[2])
            d.roll(c)

if __name__ == '__main__':
    main()


