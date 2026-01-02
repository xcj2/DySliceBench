
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

    def same(self,b):
        com1 = 'SSSWSSSE'
        com2 = 'WWWW'
        for c in com1:
            if self.dice[1]==b.dice[1]:break
            if c=='E':return False
            b.roll(c)
        for c in com2:
            if self.dice==b.dice:return True
            b.roll(c)
        return False

def main():
    n = int(input())
    dices = []
    for _ in range(n):
        dices.append(dice(list(map(int,input().split()))))
    for i in range(n):
        for j in range(i+1,n):
            if dices[i].same(dices[j]):
                print('No')
                return
    print('Yes') 

if __name__ == '__main__':
    main()


