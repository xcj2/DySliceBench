def gcd(a, b):
    r = a % b
    while r != 0:
        a, b, r = b, r, b % r
    return b

class query:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def isEternal(self):
        if self.a < self.b:
            return "No"
        if self.d < self.b:
            return "No"
        if self.b <= self.c:
            return "Yes"
        g = gcd(self.d, self.b)
        if self.b - g + self.a % g > self.c:
            return "No"
        return "Yes"

if __name__ == "__main__":
    t = int(input())
    querys = [query(*[int(s) for s in input().split()]) for _ in range(t)]
    for q in querys:
        print(q.isEternal())
