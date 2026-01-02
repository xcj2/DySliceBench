class Dice():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6
    
    
    def diceMovement(self, step):
        self.step = step
        
        if self.step == 'E':
            temp = self.s1
            self.s1 = self.s4
            self.s4 = self.s6
            self.s6 = self.s3
            self.s3 = temp
            
            
        elif self.step == 'N':
            temp = self.s1
            self.s1 = self.s2
            self.s2 = self.s6
            self.s6 = self.s5
            self.s5 = temp
            
        elif self.step == 'S':
            temp = self.s1
            self.s1 = self.s5
            self.s5 = self.s6
            self.s6 = self.s2 
            self.s2 = temp
            
        else:
            temp = self.s1
            self.s1 = self.s3
            self.s3 = self.s6
            self.s6 = self.s4
            self.s4 = temp
            
            
            
    def getTop(self):
        return self.s1
        
        
def main():
    s1,s2,s3,s4,s5,s6 = map(int, input().split())
    dice = Dice(s1,s2,s3,s4,s5,s6)
    movement = str(input())
    
    for step in movement:
        dice.diceMovement(step)
        
    print(f'{dice.getTop()}')

if __name__ == '__main__': main()
