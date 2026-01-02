from heapq import heappush, heappop

class City(object):
    def __init__(self, i, year):
        self.i = i
        self.year = year
        self.id = None

    def __lt__(self, other):
        return self.year < other.year

    def __eq__(self, other):
        return self.year == other.year

    def __gt__(self, other):
        return self.year > other.year


class Solver(object):
    def __init__(self):
        self.n, self.m = list(map(int, input().split(" ")))
        self.prefectures = [[] for _ in range(self.n)]
        self.cities = []
        for i in range(self.m):
            p, y = list(map(int, input().split(" ")))
            city = City(i+1, y)
            self.cities.append(city)
            heappush(self.prefectures[p-1], city)

    def solve(self):
        for i in range(self.n):  # For each prefecture Pi
            for j in range(len(self.prefectures[i])):  # For each Cj in Pi
                city = heappop(self.prefectures[i])
                city.id = "{:06d}{:06d}".format(i+1, j+1)
        for city in self.cities:
            print(city.id)


if __name__ == "__main__":
    s = Solver()
    s.solve()