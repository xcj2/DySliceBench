'''
Created on 2017/03/09

@author: 03key
'''

def gcd(x,y):
    if x<y:
        tmp = x
        x = y
        y = tmp
    ans = y
    if x%y != 0:
        ans = gcd(y,x%y)
    return ans

class Mobile:
    def __init__(self,leftratio=0,rightratio=0,left=-1,right=-1):
        self.weight = 0
        self.leftratio = leftratio
        self.rightratio = rightratio
        self.left = left
        self.leftweight = 0
        self.right = right
        self.rightweight = 0

    def calc(self):
        if self.weight != 0 : return self.weight

        if self.left == -1:
            self.leftweight = 1
        else:
            self.leftweight = Mobile.calc(self.left)
        if self.right == -1:
            self.rightweight = 1
        else:
            self.rightweight = Mobile.calc(self.right)

        lmoment = self.leftratio*self.leftweight
        rmoment = self.rightratio*self.rightweight
        lcs = lmoment * rmoment // gcd(lmoment,rmoment)
        self.weight = (lcs//self.leftratio) + (lcs//self.rightratio)

        return self.weight

    def stdout(self):
        print(self.left, self.right)

while True:
    n = int(input())
    if n==0: break
    barlist = [Mobile() for i in range(n)]
    for i in range(n):
        p,q,r,b = map(int, input().split())
        barlist[i].leftratio = p
        barlist[i].rightratio = q
        if r != 0 : barlist[i].left = barlist[r-1]
        if b != 0 : barlist[i].right = barlist[b-1]

    maxi = 0
    for i in range(n):
        maxi = max(barlist[i].calc(),maxi)

    print(maxi)