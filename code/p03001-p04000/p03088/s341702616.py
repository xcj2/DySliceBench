class DP:

    def __init__(self, n):
        self.memo = [{} for _ in range(n+1)]
        self.end = n
        self.mod = 10 ** 9 + 7

    def dp(self, cur, last3):
    
        if last3 in self.memo[cur]:
            return self.memo[cur][last3]
        if cur == self.end:
            return 1
        
        ret = 0
        for c in 'ACTG':
            if self.is_ok(last3 + c):
                ret = (ret + self.dp(cur + 1, last3[1:] + c)) % self.mod

        self.memo[cur][last3] = ret
        return ret

    def is_ok(self, last4):
        
        for i in range(4):
            t = list(last4)
            if i < 3:
                t[i], t[i+1] = t[i+1], t[i]
            if ''.join(t).count('AGC') > 0:
                return False
        return True


def main():

    n = int(input())
    solver = DP(n)

    print(solver.dp(0, 'CCC'))


main()
