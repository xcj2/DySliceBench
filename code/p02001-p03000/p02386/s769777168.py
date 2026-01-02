class Dice:
    def __init__(self):
        self.state =[1, 2, 3, 4, 5, 6]

    def setState(self, li):  # [top, S, E, W, N, under]
        self.state = li

    def move(self, str_direction):
        if str_direction == "N":
            self.state = [self.state[1], self.state[5],self.state[2],
                          self.state[3], self.state[0], self.state[4]]
        if str_direction == "W":
            self.state = [self.state[2], self.state[1], self.state[5],
                          self.state[0], self.state[4], self.state[3]]
        if str_direction == "E":
            self.state = [self.state[3], self.state[1], self.state[0],
                          self.state[5], self.state[4], self.state[2]]
        if str_direction == "S":
            self.state = [self.state[4], self.state[0], self.state[2],
                          self.state[3], self.state[5], self.state[1]]

    def rotate(self):
        self.state = [self.state[0], self.state[2], self.state[4],
                      self.state[1], self.state[3], self.state[5]]

    def sameDice1(self, dice1):
        set1 = list()
        for _ in range(4):
            for __ in range(4):
                set1.append(self.state)
                self.rotate()
            self.move("N")
        self.move("E")
        for _ in range(4):
            set1.append(self.state)
            self.rotate()
        self.move("E")
        self.move("E")
        for _ in range(4):
            set1.append(self.state)
            self.rotate()
        if dice1.state in set1:
            return "Yes"
        return "No"


def main():
    n = int(input())
    dices = []
    for i in range(n):
        dices.append(Dice())
        dices[i].setState(list(map(int, input().split())))
    bl = False
    result = "Yes"
    for i in range(n):
        for j in range(n):
            if i == j:
                break
            if dices[i].sameDice1(dices[j]) == "Yes":
                result = "No"
                bl = True
                break
        if bl:
            break
    print(result)

if __name__ == "__main__":
    main()