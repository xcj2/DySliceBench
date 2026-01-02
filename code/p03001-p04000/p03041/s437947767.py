import copy

class Solver:
    def __init__(self, _n, _k, _s):
        self.n = _n
        self.k = _k
        self.upper = copy.deepcopy(_s)
        self.lower = _s.lower()

        self.solve()
    
    def solve(self):
        ans = ""
        for i in range(self.n):
            if i == self.k - 1:
                ans = ans + self.lower[i]
            else:
                ans = ans + self.upper[i]
        
        print(ans)

def main():
    n, k = (int(i) for i in input().split())
    s=input()
    Solver(n, k, s)



if __name__ == "__main__":
    main()