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

def main():
    d = dice(list(map(int,input().split())))
    com = input()
    for c in com:
        if c == 'N':d.roll_n()
        if c == 'E':d.roll_e()
        if c == 'S':d.roll_s()
        if c == 'W':d.roll_w()
    print(d.top())

if __name__ == '__main__':
    main()


