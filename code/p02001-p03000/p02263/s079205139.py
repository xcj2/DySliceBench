#逆ポーランド記法(Reverse Polish Notation, RPN)
class RPN():
    def __init__(self):
        self.top = 0
        self.S = []
        self.MAX = 100

    def isEmpty(self):
        return self.top == 0

    def isFull(self):
        #return self.top >= self.MAX - 1
        return self.top >= self.MAX

    def push(self,x):
        if self.isFull():
            raise ValueError("オーバーフロー")
        self.top+=1
        self.S.append(x)

    def pop(self):
        if self.isEmpty():
            raise ValueError("アンダーフロー")
        self.top-=1
        #print("self.top:{}".format(self.top))
        #print("S:{}".format(self.S))
        return self.S.pop(self.top)


X = input().split(" ")
rpn = RPN()
for x in X:
    #print(x)
    if x.isnumeric():
        #print("num")
        rpn.push(x)
    else:
        #print("dig")
        num_2 =rpn.pop()
        num_1 =rpn.pop()
        res = eval(str(num_1) + x + str(num_2))
        rpn.push(res)

print(rpn.pop())
