class triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def calc(self):
        a = int(self.a**2)
        b = int(self.b**2)
        c = int(self.c**2)

        if (a+b == c) or (b+c == a) or (a+c == b):
            return True
        else:
            return False

    def print(self):
        ans = self.calc()
        if ans:
            print("YES")
        else:
            print("NO")

def main():
    data = []
    array_size = int(input())

    for i in range(array_size):
        n = input().split()
        a = int(n[0])
        b = int(n[1])
        c = int(n[2])

        data.append(triangle(a,b,c))

    for array in data:
        array.print()

if __name__ == "__main__":
    main()