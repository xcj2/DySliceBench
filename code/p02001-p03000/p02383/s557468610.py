class State:
    d = {
        "E": lambda l: zip((0, 2, 3, 5), (l[3], l[0], l[5], l[2])),
        "N": lambda l: zip((0, 1, 4, 5), (l[1], l[5], l[0], l[4])),
        "S": lambda l: zip((0, 1, 4, 5), (l[4], l[0], l[5], l[1])),
        "W": lambda l: zip((0, 2, 3, 5), (l[2], l[5], l[0], l[3]))
        }

    def __init__(self, s, t):
        self.pos = list(range(1, 7))
        self.pip = s.split()
        self.log = t

    def __call__(self):
        for c in self.log:
            for i, v in self.d[c](self.pos):
                self.pos[i] = v

    def __str__(self):
        return self.pip[self.pos[0]-1]

state = State(input(), input())
state()
print(state)