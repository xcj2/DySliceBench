class Dice:
    def __init__(self,list):
        self.list = []
        for i in range(6):
            self.list.append(list[i])

    def rotate(self,dir):
        if dir == "N":
            self.list[0], self.list[1], self.list[5], self.list[4] = self.list[1], self.list[5], self.list[4], self.list[0]
        elif dir == "S":
            self.list[0], self.list[4], self.list[5], self.list[1] = self.list[4], self.list[5], self.list[1], self.list[0]
        elif dir == "W":
            self.list[0], self.list[3], self.list[5], self.list[2] = self.list[2], self.list[0], self.list[3], self.list[5]
        elif dir == "E":
            self.list[0], self.list[3], self.list[5], self.list[2] = self.list[3], self.list[5], self.list[2], self.list[0]
        elif dir == "H":
            self.list[1], self.list[2], self.list[4], self.list[3] = self.list[2], self.list[4], self.list[3], self.list[1]
        elif dir =="V":
            self.list[0], self.list[3], self.list[5], self.list[2] = self.list[3], self.list[5], self.list[2], self.list[0]
        else:
            pass

    def show(self):
        print("D:{}".format(repr(self.list)))

    def isface(self,f):
        if f in self.list:
            return True
        else:
            return False

    def isSameface(self,b):
        for i in range(len(self.list)):
            if self.list[i] != b.list[i]:
                return False
        return True

    def isSame(self,b):
        for c in "zHHHWHHHEHHHEHHHWHHHWHHH":
            b.rotate(c)
            if self.isSameface(b):
                return True
        return False


def main():
    num = int(input())
    dice =[]
    for i in range(num):
        l = [int(x) for x in input().split()]
        dice.append(Dice(l))

    for i in range(num):
        for j in range(i+1,num):
            if dice[i].isSame(dice[j]):
                print("No")
                exit(0)

    print("Yes")


if __name__  == '__main__':
    main()

