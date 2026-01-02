import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)

class Solve:
    def __init__(self):
        self.flag = False

    def helper(self, a, b, c, k):
        if k == 0:
            if b > a and c > b:
                self.flag = True
                return
            else:
                return
        else:
            self.helper(a * 2, b, c, k - 1)
            self.helper(a, b * 2, c, k - 1)
            self.helper(a, b, c * 2, k - 1)


def main():
    a,b,c = [int(i) for i in input().strip().split()]
    k = int(input().strip())
    
    solver = Solve()

    solver.helper(a, b, c, k)
    if solver.flag:
        print("Yes")
    else:
        print("No")



    return

if __name__ == "__main__":
    main()
