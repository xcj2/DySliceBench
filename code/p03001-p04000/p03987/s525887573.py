class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[A[i]] = i

    uni = UnionFind(N)
    ans = 0
    for i in range(N, 0, -1):
        k = B[i]
        left = 0
        right = 0
        if k - 1 >= 0 and A[k-1] > A[k]:
            left = uni.size(uni.find(k-1))
            uni.union(k-1,k)
        if k + 1 <= N - 1 and A[k+1] > A[k]:
            right = uni.size(uni.find(k+1))
            uni.union(k+1,k)

        ans += (left+1) * (right+1) * A[k]

    print(ans)




if __name__ == "__main__":
    main()