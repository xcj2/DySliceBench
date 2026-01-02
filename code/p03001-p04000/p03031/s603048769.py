import sys
input = sys.stdin.readline


class Lights:

    def __init__(self):
        self.lights = []

    def add(self, light):
        self.lights.append(light)

    def is_all_up(self, switch):
        for light in self.lights:
            if not light.is_up(switch):
                return False
        return True

    def __str__(self):
        result = "{"
        for light in self.lights:
            result += str(light)
        return result + "}"


class Light:

    def __init__(self, k, s, p):
        self.k = k
        self.s = s
        self.p = p

    def is_up(self, switch):
        intersection = self.s.intersection(switch)
        return self.p == len(intersection) % 2

    def __str__(self):
        return "[k={}, s={}, p={}]".format(self.k, self.s, self.p)


def main():
    n, m = map(int, input().split())
    ks_lst = [list(map(int, input().split())) for _ in range(m)]
    p_lst = list(map(int, input().split()))
    lights = Lights()
    for ks, p in zip(ks_lst, p_lst):
        k, s = ks[0], set(ks[1:])
        lights.add(Light(k, s, p))

    ans = 0
    for bit in range(2**n):
        switches = set()
        for i in range(n+1):
            if (bit >> i) & 1:
                switches.add(i+1)
        if lights.is_all_up(switches):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
