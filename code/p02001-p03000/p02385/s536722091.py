class Dice:
    def __init__(self,s):
        self.start = [0,1,2,4,3,5]#上 正 右 后 左 下
        self.s = s
        
    #下面的是几个反转方式
    def N(self):
        self.start[0],self.start[1],self.start[3],self.start[5] = \
        self.start[1],self.start[5],self.start[0],self.start[3]
        
    def S(self):
        self.start[0],self.start[1],self.start[3],self.start[5] = \
        self.start[3],self.start[0],self.start[5],self.start[1]
        
    def W(self):
        self.start[0],self.start[2],self.start[4],self.start[5] = \
        self.start[2],self.start[5],self.start[0],self.start[4]
    
    def E(self):
        self.start[0],self.start[2],self.start[4],self.start[5] = \
        self.start[4],self.start[0],self.start[5],self.start[2]    


    #这是特殊的旋转方法
    def roll(self):
        self.start[1],self.start[2],self.start[3],self.start[4] = \
        self.start[4],self.start[1],self.start[2],self.start[3]          
    
    def get_top(self):
        return self.s[self.start[0]]
    
    def get_zhengMian(self):
        return self.s[self.start[1]]
    
    def get_right(self):
        return self.s[self.start[2]]
    
    def get_left(self):
        return self.s[self.start[4]]  
    
def is_same(dice1,dice2):
    FLAG = False
    dice1 = Dice(dice1)
    dice2 = Dice(dice2)
    a,b,c = dice1.get_top(),dice1.get_zhengMian(),dice1.get_right()
    d,e,f = dice2.get_top(),dice2.get_zhengMian(),dice2.get_right()
    
    #我们在这只是转动dice2
    #让上面保持一致
    if d==a:
        FLAG = True
    elif d!=a:
        tmp1,tmp2 = dice2.get_left(),dice2.get_right()
        if tmp1==a:
            dice2.E()
            FLAG = True
        elif tmp2==a:
            dice2.W()
            FLAG = True
        else:
            count = 0
            while True:
                count += 1
                tmp1 = dice2.get_top()
                if tmp1==a:
                    FLAG = True
                    break
                if count == 4:
                    break
                dice2.S()
    
    #让正面保持一致
    if FLAG==False:
        return FLAG
    b,e = dice1.get_zhengMian(),dice2.get_zhengMian()
    if e==b:
        FLAG = True
    elif e!=b:
        count = 0
        while True:
            count += 1
            tmp = dice2.get_zhengMian()
            if tmp==b:
                FLAG = True
                break
            if count==4:
                FLAG = False
                break
            dice2.roll()
    
    if FLAG==False:
        return FLAG
    else:
        f = dice2.get_right()
        if f==c:
            return True
        else:
            return False

if __name__=="__main__":
    dice1 = list(map(int,input().split()))
    dice2 = list(map(int,input().split()))
    tmp1 = dice1.copy();tmp2 = dice2.copy()
    tmp1.sort();tmp2.sort()
    num = 0;
    for i in range(1,6):
        if tmp1[i-1]!=tmp1[i]:
            num += 1
    if num<=2:
        print('Yes')
    else:
        bl = is_same(dice1, dice2)
        if bl == True:
            print('Yes')
        else:
            print('No')
