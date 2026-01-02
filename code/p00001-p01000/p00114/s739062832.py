def mcd(m,n):
    if n==0:
        return(m)
    else:
        r = m % n
    return(mcd(n,r))

def lcd(m,n):
    return(m * n // mcd(m, n))

class Fry:
    def __init__(self,a1,m1,a2,m2,a3,m3):
        self.a1 = a1
        self.m1 = m1
        self.a2 = a2
        self.m2 = m2
        self.a3 = a3
        self.m3 = m3


    def test(self,a,m):
        n = 0
        x = 1
        while True:
            x1 = (a * x) % m
            n += 1
            if x1 == 1:
                break
            else:
                x = x1
        return(n)

    def mv(self):
        n1 = self.test(self.a1,self.m1)
        n2 = self.test(self.a2,self.m2)
        n3 = self.test(self.a3,self.m3)
        m1 = lcd(n1,n2)
        m2 = lcd(m1,n3)

        return(m2)

while True:
    a1,m1,a2,m2,a3,m3 = list(map(int, input().strip().split()))
    if a1==m1==a2==m2==a3==m3==0:
        break
    fry = Fry(a1,m1,a2,m2,a3,m3)
    print(fry.mv())