class Dice:
    def __init__(self, faces = None):
        self.dice = {'N':2, 'E':4, 'S':5, 'W':3}
        self.faces = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6}
        self.currTop = 1
        if faces is not None:
            self.faces = faces

    def top(self):
        return self.currTop

    def topFace(self):
        return self.faces[self.currTop]

    def bottom(self):
        return 7 - self.currTop

    def bottomFace(self):
        return self.faces[self.bottom()]

    def rot(self, direction):
        newTop = self.dice[direction]
        currTop = self.currTop
        self.currTop = newTop
        if direction == 'N':
            self.dice['N'] = 7 - currTop
            self.dice['S'] = currTop
        elif direction == 'S':
            self.dice['N'] = currTop
            self.dice['S'] = 7 - currTop
        elif direction == 'E':
            self.dice['E'] = 7 - currTop
            self.dice['W'] = currTop
        elif direction == 'W':
            self.dice['E'] = currTop
            self.dice['W'] = 7 - currTop

    def yaw(self, direction):
        newDice = {}
        if direction == 'E':
            newDice['N'] = self.dice['E']
            newDice['E'] = self.dice['S']
            newDice['S'] = self.dice['W']
            newDice['W'] = self.dice['N']
        if direction == 'W':
            newDice['N'] = self.dice['W']
            newDice['E'] = self.dice['N']
            newDice['S'] = self.dice['E']
            newDice['W'] = self.dice['S']
        self.dice = newDice

dbg = False

faces1 = {k:v for k,v in zip(range(1,7), map(int, input().split()))}
faces2 = {k:v for k,v in zip(range(1,7), map(int, input().split()))}

d1 = Dice(faces1)
d2 = Dice(faces2)

d2indexes = [d2index for d2index,d2face in d2.faces.items() if d1.topFace() == d2face]

for d2topIndex in d2indexes:
    if dbg: print('d2topIndex:%d' % (d2topIndex) )

    # search d1.topFace() in d2 and rotate to make d2.topFace() equal to d1.topFace().
    key = [k for k,v in d2.dice.items() if d2topIndex == v]
    if len(key) == 0:
        d2.rot('N')
        key = [k for k,v in d2.dice.items() if d2topIndex == v]
    d2.rot(key[0])

    if d1.topFace() != d2.topFace() or d1.bottomFace() != d2.bottomFace():
        continue

    # rotate(yaw) to make frontIdx front.
    cnt = 0
    while True:
        if dbg: print('cnt:%d' % (cnt) )
        if cnt > 4:
            break
        d2.yaw('E')
        cnt += 1

        # compare two dices.
        d1State = {k:d1.faces[v] for k,v in d1.dice.items()}
        d2State = {k:d2.faces[v] for k,v in d2.dice.items()}
        if d1State == d2State:
            print('Yes')
            exit()

print('No')