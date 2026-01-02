class Dice:
    def __init__(self, x):
        self.top = x[0]
        self.front = x[1]
        self.right = x[2]
        self.left = x[3]
        self.back = x[4]
        self.bottom = x[5]

    def N(self):
        self.top, self.front, self.bottom, self.back = self.front, self.bottom, self.back, self.top

    def E(self):
        self.top, self.right, self.bottom, self.left = self.left, self.top, self.right, self.bottom

    def S(self):
        self.top, self.front, self.bottom, self.back = self.back, self.top, self.front, self.bottom

    def W(self):
        self.top, self.right, self.bottom, self.left = self.right, self.bottom, self.left, self.top

    def up_front_to_right(self, top, front):
        if (top, front) in [(self.top, self.front), (self.front, self.bottom), (self.bottom, self.back), (self.back, self.top)]:
            return self.right
        elif (top, front) in [(self.front, self.top), (self.bottom, self.front), (self.back, self.bottom), (self.top, self.back)]:
            return self.left
        elif (top, front) in [(self.left, self.front), (self.front, self.right), (self.right, self.back), (self.back, self.left)]:
            return self.top
        elif (top, front) in [(self.front, self.left), (self.right, self.front), (self.back, self.right), (self.left, self.back)]:
            return self.bottom
        elif (top, front) in [(self.top, self.left), (self.left, self.bottom), (self.bottom, self.right), (self.right, self.top)]:
            return self.front
        elif (top, front) in [(self.left, self.top), (self.bottom, self.left), (self.right, self.bottom), (self.top, self.right)]:
            return self.back
        else:
            return -1
            
    def inverse(self,a):
        if a==self.top:
            return self.bottom
        elif a==self.front:
            return self.back
        elif a==self.right:
            return self.left
        elif a==self.left:
            return self.right
        elif a==self.back:
            return self.front
        elif a==self.front:
            return self.back
        else:
            return -1
            
*x,=map(int,input().split())
*y,=map(int,input().split())
dice0=Dice(x)
dice1=Dice(y)
for i in x:
    for j in x:
        if i!=j and i!=dice0.inverse(j):
            a=dice0.up_front_to_right(i,j)
            b=dice1.up_front_to_right(i,j)
            if a!=b:
                print('No')
                exit()
print('Yes')
            
