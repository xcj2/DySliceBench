import sys

class Imos1D:
    def __init__(self,sz):
        self.__seq = [0] * sz

    def update(self, a, b): # [a,b)
        self.__seq[a] += 1
        self.__seq[b] -= 1

    def calc(self):
        for i in range(len(self.__seq) - 1):
            self.__seq[i + 1] += self.__seq[i]

    def get(self,i):
        return self.__seq[i]

def main():
    n = int(input())
    imos = Imos1D(1000000 + 10)

    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        imos.update(a, b + 1)

    imos.calc()

    # solve
    ans = 1
    for i in range(n + 2):
        if imos.get(i) >= i - 1:
            ans = max(ans, i)

    print(ans - 1) # ???????????????


if __name__ == '__main__':
    main()