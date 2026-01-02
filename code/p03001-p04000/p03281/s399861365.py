from collections import Counter
class Solver(object):
    def __init__(self):
        self.n = int(input())
        self.primes = Solver.generate_primes(self.n)

    def solve(self):
        count = 0
        for i in range(2, self.n+1):
            if i % 2 != 0:
                factors = self.prime_factorize(i)
                if len(set(factors)) == len(factors):
                    if self.has_eight(factors):
                        # print(i, factors)
                        count += 1
                else:
                    c = Counter(factors)
                    s = list(c.keys())
                    if len(s) == 2:
                        if (c[s[0]] == 1) and (c[s[1]] == 3) or ((c[s[0]] == 3) and (c[s[1]] == 1)):
                            # print(i, factors)
                            count += 1

        print(count)
    
    def has_eight(self, factors):
        return len(set(factors)) == 3

    def prime_factorize(self, n):
        factor = []
        for i in self.primes:
            if i > n:
                break
            if n % i == 0:
                factor.append(i)
                n = int(n/i)
                while n % i == 0:
                    factor.append(i)
                    n = int(n/i)
        return factor

    @staticmethod
    def generate_primes(length):
        """Generate prime from 1 to length, inclusive"""
        primes = []
        if length < 2:
            return primes
        numbers = range(2, length+1)  # 2 .. length
        i = numbers[0]
        while True:
            primes.append(i)
            new_numbers = []
            for j in numbers:
                if j % i != 0:
                    new_numbers.append(j)
            numbers = new_numbers
            if len(numbers) == 0:
                break
            i = numbers[0]
        return primes


if __name__ == "__main__":
    s = Solver()
    s.solve()