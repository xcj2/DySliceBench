from bisect import bisect

class Solver(object):
    def __init__(self):
        self.n = int(input())
        self.t, self.a = list(map(int, input().split(" ")))
        self.locations = list(map(int, input().split(" ")))
        self.locations = [(x+1, self.t - (0.006*y)) for (x, y) in enumerate(self.locations)]
        self.locations.sort(key=lambda x: x[1])

    def solve(self):
        temps = [y for x, y in self.locations]
        b = bisect(temps, self.a)
        if b >= len(temps):
            print(self.locations[b-1][0])
        else:
            left = abs(self.a - self.locations[b-1][1])
            right = abs(self.a - self.locations[b][1])
            if left < right:
                print(self.locations[b-1][0])
            else:
                print(self.locations[b][0])

    def debug(self):
        for x in self.locations:
            print(x)


if __name__ == "__main__":
    s = Solver()
    s.solve()