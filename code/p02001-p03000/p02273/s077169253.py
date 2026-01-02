import math
class Dot:
    x=0.0
    y=0.0
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __lt__(self,other):
        return self.x < other.x
    def print(self):
        x=self.x
        y=self.y
        print("{:.8f} {:.8f}".format(x,y))       
def kock(n,a,b,dots):
    if n == 0:
        return
    s=Dot((2*a.x+b.x)/3,(2*a.y+b.y)/3)
    t=Dot((a.x+2*b.x)/3,(a.y+2*b.y)/3)
    rad=math.radians(60)
    x=(t.x-s.x)*math.cos(rad)-(t.y-s.y)*math.sin(rad)+s.x
    y=(t.x-s.x)*math.sin(rad)+(t.y-s.y)*math.cos(rad)+s.y
    u=Dot(x,y)

    kock(n-1,a,s,dots)
    s.print()
    dots.append(s)
    kock(n-1,s,u,dots)
    u.print()
    dots.append(u)
    kock(n-1,u,t,dots)
    t.print()
    dots.append(t)
    kock(n-1,t,b,dots)

if __name__ == "__main__":
    n=int(input())
    dots=[]
    dot1=Dot(0,0)
    dot2=Dot(100,0)
    dots.append(dot1)
    dots.append(dot2)
    dot1.print()
    kock(n,dot1,dot2,dots)
    dot2.print()
