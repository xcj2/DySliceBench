import sys
input = sys.stdin.readline

class Dice:
    def __init__(self, u, d, w, e, n, s):
        self.nums = {
            "u": u,
            "d": d,
            "w": w,
            "e": e,
            "n": n,
            "s": s
        }
    
    def roll_w(self):
        dic = {}
        dic["s"] = self.nums["s"]
        dic["n"] = self.nums["n"]
        dic["w"] = self.nums["u"]
        dic["u"] = self.nums["e"]
        dic["e"] = self.nums["d"]
        dic["d"] = self.nums["w"]
        self.nums = dic
    
    def roll_e(self):
        dic = {}
        dic["s"] = self.nums["s"]
        dic["n"] = self.nums["n"]
        dic["w"] = self.nums["d"]
        dic["d"] = self.nums["e"]
        dic["e"] = self.nums["u"]
        dic["u"] = self.nums["w"]
        self.nums = dic
    
    def roll_s(self):
        dic = {}
        dic["w"] = self.nums["w"]
        dic["e"] = self.nums["e"]
        dic["s"] = self.nums["u"]
        dic["u"] = self.nums["n"]
        dic["n"] = self.nums["d"]
        dic["d"] = self.nums["s"]
        self.nums = dic
    
    def roll_n(self):
        dic = {}
        dic["w"] = self.nums["w"]
        dic["e"] = self.nums["e"]
        dic["n"] = self.nums["u"]
        dic["u"] = self.nums["s"]
        dic["s"] = self.nums["d"]
        dic["d"] = self.nums["n"]
        self.nums = dic
    

def main():
    a = list(map(int, input().split()))
    s = input().strip()

    dice = Dice(a[0], a[5], a[3], a[2], a[4], a[1])

    for c in s:
        if c == "S":
            dice.roll_s()
        elif c == "W":
            dice.roll_w()
        elif c == "N":
            dice.roll_n()
        elif c == "E":
            dice.roll_e()
    
    print(dice.nums["u"])



if __name__ == "__main__":
    main()
