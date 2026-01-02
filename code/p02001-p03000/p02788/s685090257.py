import sys

sys.setrecursionlimit(500000)
def input():
    return sys.stdin.readline()[:-1]

class BIT:
            
    def __init__(self, L):
        self.N = len(L)
        self.bit = [0]*self.N
        for i,l in enumerate(L):
            self.add(i,l)

    def add(self, a, w):
        x = a + 1
        for i in range(1000):
            self.bit[x-1] += w
            x += x & -x
            if x > self.N:
                break

    def sum(self, a):
        x = a+1
        ret = 0
        for i in range(1000):
            ret += self.bit[x-1]
            x -= x & -x
            if x <= 0:
                break        
        return ret




def main():
    N,D,A = list(map(int,input().split()))

    enemy = []
    for i in range(N):
        x,h = list(map(int,input().split()))
        if h%A==0:
            enemy.append([x,h//A])
        else:
            enemy.append([x,h//A+1])

    enemy.sort(key=lambda x:x[0])
    def bisect(index):
        x = enemy[index][0]
        if enemy[N-1][0] <= x + 2*D:
            return N-1
        l = index
        r = N-1
        while r-l>1:
            if enemy[(r+l)//2][0] <= x + 2*D:
                l = (r+l)//2
            else:
                r = (r+l)//2
        return l

    bit = BIT([0]*N)

    count1 = 0
    for i in range(N):
        if i>0:
            v = bit.sum(N-1) - bit.sum(i-1)
        else:
            v=0
        if enemy[i][1] - v>0:
            count1 += enemy[i][1] - v
            j = bisect(i)
            bit.add(j,enemy[i][1] - v)

    enemy = enemy[::-1]
    for i in range(N):
        enemy[i][0] = -enemy[i][0]

    bit = BIT([0]*N)

    count2 = 0
    for i in range(N):
        if i>0:
            v = bit.sum(N-1) - bit.sum(i-1)
        else:
            v = 0
        if enemy[i][1] - v>0:
            count2 += enemy[i][1] - v
            j = bisect(i)
            bit.add(j,enemy[i][1] - v)


    print(min(count1,count2))

if __name__ == '__main__':
    main()

