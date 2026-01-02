class Plan(object):
    def __init__(self, m):
        self.plans = [-1] * (m + 1)
        self.size = m

    def reserve(self, a, b):
        a = self.find_empty(a)
        if a == -1:
            return
        self.plans[a] = [b, a+1]

    def find_empty(self, a):
        if a > self.size:
            return -1
        if self.plans[a] == -1:
            return a
        next_day = self.find_empty(self.plans[a][1])
        if next_day == -1:
            return -1
        self.plans[a][1] = next_day
        return next_day


def main():
    n, m = map(int, input().split())
    w = [list(map(int, input().split())) for _ in range(n)]
    wsorted = sorted(w, key=lambda x: x[1], reverse=True)
    plan = Plan(m)
    for work in wsorted:
        plan.reserve(*work)

    print(sum([p[0] for p in plan.plans if p != -1]))


main()
