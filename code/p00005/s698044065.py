class GCD():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def gcd(self):
        if self.a < self.b:
            self.a, self.b = self.b, self.a
        while self.b:
            self.a, self.b= self.b, self.a % self.b

        return self.a

    def print(self):
        lcm = self.a * self.b // self.gcd()
        print(self.gcd(), lcm)

def main():
    data =[]

    while 1:
        try:
            n = input().split()

            a = int(n[0])
            b = int(n[1])

            data.append(GCD(a, b))

        except EOFError:
            break

    for array in data:
        array.print()

if __name__ == "__main__":
    main()
