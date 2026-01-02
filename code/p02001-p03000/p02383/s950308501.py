def main():
    one, two, three, four, five, six = map(lambda n: int(n), input().split(' '))
    d = Dice(one, two, three, four, five, six)
    s = input()
    for i in s:
        d.roll(i)
    print(d.top)

class Dice:
    def __init__(self, one, two, three, four, five, six):
        self.top = one
        self.bottom = six
        self.s = two
        self.n = five
        self.e = three
        self.w = four 
    

    def roll(self, d):
        top = self.top
        bottom = self.bottom
        s = self.s
        n = self.n
        e = self.e
        w = self.w
        if d == "S":
            self.bottom = s
            self.s = top
            self.top = n
            self.n = bottom
        elif d == "N":
            self.bottom = n
            self.s = bottom
            self.top = s
            self.n = top
        elif d == "W":
            self.bottom = w
            self.w = top
            self.top = e
            self.e = bottom
        else:
            self.bottom = e
            self.e = top
            self.top = w
            self.w = bottom
        

if __name__ == "__main__":
    main()
