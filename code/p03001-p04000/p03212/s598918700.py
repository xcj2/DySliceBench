class Handle753:
    def __init__(self, N):
        self.N = N
        self.ans = 0


    def judge753(self, x):
        counter = [False for _ in range(10)]
        while x > 0:
            a = x % 10
            counter[a] = True
            x //= 10

        for j, c in enumerate(counter):
            if j in (3, 5, 7):
                if not c:
                    return False
            else:
                if c:
                    return False
        
        return True


    def dfs(self, x=0):
        if x > self.N:
            return
        if self.judge753(x):
            self.ans += 1
        self.dfs(10 * x + 3)
        self.dfs(10 * x + 5)
        self.dfs(10 * x + 7)


    def show_answer(self):
        print(self.ans)


def main():
    N = int(input())
    hoge = Handle753(N)
    hoge.dfs()
    hoge.show_answer()


if __name__ == "__main__":
    main()
