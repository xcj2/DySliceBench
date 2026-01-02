import math

class Calc:
    def __init__(self,a,op,b):
        self.a = a
        self.b = b
        self.op = op

    def calc(self):
        if self.op == "+":
            return self.a + self.b
        elif self.op == "-":
            return self.a - self.b
        elif self.op == "*":
            return self.a * self.b
        elif self.op == "/":
            try:
                ans = self.a / self.b
            except ZeroDivisionError:
                return 0
            else:
                return ans
        else:
            return "Invalid Operator."

def main():
    data = []
    while 1:
        n = input().split()
        a = int(n[0])
        op = n[1]
        b = int(n[2])
        if op == "?":
            break

        data.append(Calc(a,op,b))

    for i in data:
        print(int(i.calc()))

if __name__ == "__main__":
    main()