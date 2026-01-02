class Dice:
    def __init__(self,t,f,r,l,ba,bo):
        self.t = t
        self.f = f
        self.r = r
        self.l = l
        self.ba = ba
        self.bo = bo
    
    def E(self):
        a = self.t
        b = self.r
        c = self.bo
        d = self.l
        self.r = a
        self.bo = b
        self.l = c
        self.t = d
    
    def N(self):
        a = self.t
        b = self.ba
        c = self.bo
        d = self.f
        self.ba = a
        self.bo = b
        self.f = c
        self.t = d
    
    def S(self):
        a = self.t
        b = self.ba
        c = self.bo
        d = self.f
        self.f = a
        self.t = b
        self.ba = c
        self.bo = d
    
    def W(self):
        a = self.t
        b = self.r
        c = self.bo
        d = self.l
        self.l = a
        self.t = b
        self.r = c
        self.bo = d

def hantei(dice1,dice2):
    global flag
    if dice1.t == dice2.f:
        dice2.N()
    elif dice1.t == dice2.r:
        dice2.W()
    elif dice1.t == dice2.l:
        dice2.E()
    elif dice1.t == dice2.ba:
        dice2.S()
    elif dice1.t == dice2.bo:
        dice2.E()
        dice2.E()
    if dice1.bo != dice2.bo:
        dice2.N()
        for i in range(4):
            if dice1.t == dice2.t and dice1.bo == dice2.bo:
                break
            dice2.E()
    for i in range(4):
        if dice1.t == dice2.t and dice1.f == dice2.f and dice1.r == dice2.r and dice1.l == dice2.l and dice1.ba == dice2.ba and dice1.bo == dice2.bo:
            flag = 1
            break
        dice2.N()
        dice2.E()
        dice2.S()
        

n = int(input())
dice = []
flag = 0
for i in range(n):
    s = input().split(" ")
    dice.append(Dice(s[0],s[1],s[2],s[3],s[4],s[5]))
hantei(dice[0],dice[1])
for i in range(n-1):
    if flag == 1:
        break
    for j in range(i+1,n):
        hantei(dice[i],dice[j])
        if flag == 1:
            break

if flag == 1:
    print("No")
else:
    print("Yes")