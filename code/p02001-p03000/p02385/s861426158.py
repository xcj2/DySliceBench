class Dice:
    def __init__(self,l1,l2,l3,l4,l5,l6):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4
        self.l5 = l5
        self.l6 = l6
        self.top = 1
        self.front = 2
        self.right = 3

    def get_top(self):
        return eval("self." + 'l' + str(self.top))

    def get_right(self):
        return eval("self." + 'l' + str(self.right))

    def get_front(self):
        return eval("self." + 'l' + str(self.front))

    def get_bottom(self):
        return eval("self." + 'l' + str(7-self.top))

    def get_left(self):
        return eval("self." + 'l' + str(7-self.right))

    def get_back(self):
        return eval("self." + 'l' + str(7-self.front))

    def rot(self):
        self.front,self.right = self.right,7-self.front

    def move(self, order):
        if order == 'S':
            pretop = self.top
            self.top = 7 - self.front
            self.front = pretop
        elif order == 'E':
            pretop = self.top
            self.top = 7 - self.right
            self.right = pretop


def match_top(dice,target):
    for i in range(4):
        dice.move('S')
        if dice.get_top() == target:
            return dice
    return False


l = list(map(int,input().split()))
d1 = Dice(l[0],l[1],l[2],l[3],l[4],l[5])

l = list(map(int,input().split()))
d2 = Dice(l[0],l[1],l[2],l[3],l[4],l[5])

d1_top = d1.get_top()
d1_front = d1.get_front()
d1_right = d1.get_right()
d1_bottom = d1.get_bottom()
d1_back = d1.get_back()
d1_left = d1.get_left()
ret = match_top(d2,d1_top)

if ret == False:
    d2.move('E')
    ret = match_top(d2,d1_top)
if ret == False:
    print('No')
else:
    matched = False
    for i in range(4):
        d2.rot()
        if d2.get_front() == d1_front and \
        d2.get_right() == d1_right and \
        d2.get_bottom() == d1_bottom and \
        d2.get_left() == d1_left and \
        d2.get_back() == d1_back:
            matched = True
            print ('Yes')
            break
    if not matched:
        print('No')