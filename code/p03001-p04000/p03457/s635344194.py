class AtCoDeer:
    def __init__(self):
        self.pos = {"x": 0, "y": 0}
        self.time = 0

    def move(self, to_x, to_y):
        self.pos = {"x": to_x, "y": to_y}
        return self.pos

    def can_move(self, t, to_x, to_y):
        dx = abs(to_x-self.pos.get("x"))
        dy = abs(to_y-self.pos.get("y"))
        total_move = dx + dy
        dt = t - self.time

        if dt < total_move:
            return False
        elif (dt-total_move) % 2 != 0:
            return False
        else:
            self.move(to_x, to_y)
            self.time = t
            return True


def main():
    n = int(input())
    at_co_deer = AtCoDeer()

    while(at_co_deer.can_move(*[int(x) for x in input().split()])):
        n -= 1
        if n == 0:
            break
    
    # 計画破綻判明後のデータ読み捨て
    for i in range(n-1):
        input()

    if n == 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()