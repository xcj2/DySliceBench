class FutureMath:
    def gcd(self, a, b):
        if a < b:
            return self.gcd(b, a)
        if b == 0:
            return a
        while b:
            a, b = b, a % b
        return a

    def gcd_(self, list):
        result = list[0]
        for el in list[1:]:
            result = self.gcd(result, el)
        return result

    def lcm(self, a, b):
        return a * b // self.gcd(a, b)

    def lcm_(self, list):
        result = list[0]
        for el in list[1:]:
            result = self.lcm(result, el)
        return result

    def divisors(self, n):
        result = list()
        for i in range(1, n+1):
            if n % i == 0:
                result.append(i)
        return result


def LI(): return list(map(int, input().split()))

fm = FutureMath()


a, b, c, d = LI()
B = b - (b//c + b//d - b//fm.lcm(c, d))
A = a - (a//c + a//d - a//fm.lcm(c, d))
border = 1 - int((a % c == 0) or (a % d == 0))
print(B - A + border)
