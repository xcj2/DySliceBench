class Dice():
    def __init__(self, numbers):
        self.top = numbers[0]
        self.s = numbers[1]
        self.e = numbers[2]
        self.w = numbers[3]
        self.n = numbers[4]
        self.bot = numbers[5]
    def rot(self, dir):
        top, s, e, w, n, bot = (self.top, self.s, self.e, self.w, self.n, self.bot)
        if dir == 'N':
            self.top = s
            self.s = bot
            self.e = e
            self.w = w
            self.n = top
            self.bot = n
        elif dir == 'S':
            self.top = n
            self.s = top
            self.e = e
            self.w = w
            self.n = bot
            self.bot = s
        elif dir == 'E':
            self.top = w
            self.s = s
            self.e = top
            self.w = bot
            self.n = n
            self.bot = e
        elif dir == 'W':
            self.top = e
            self.s = s
            self.e = bot
            self.w = top
            self.n = n
            self.bot = w
    def getTop(self):
        return self.top
    def rotMany(self, command):
        for dir in command:
            self.rot(dir)



li = list(map(int, input().split()))
D1 = Dice(li)
li = list(map(int, input().split()))
D2 = Dice(li)

cmd_list = [
    "SEN", "SEN", "SEN", "SENN",
    "SEN", "SEN", "SEN", "SENN",
    "SEN", "SEN", "SEN", "SENN",
    "SEN", "SEN", "SEN", "SENE",
    "SEN", "SEN", "SEN", "SENEE",
    "SEN", "SEN", "SEN", ""
]

for cmd in cmd_list:
    if D1.top == D2.top and D1.s == D2.s and D1.w == D2.w and D1.e == D2.e and D1.n == D2.n and D1.bot == D2.bot:
        print("Yes")
        exit(0)
    else:
        D1.rotMany(cmd)
print("No")

