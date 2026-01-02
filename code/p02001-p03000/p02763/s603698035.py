class BinaryIndexedTree():
    def __init__(self, num):
        self.bit = [0]*(num+1) # 1-indexed
        self.num = num

    def sum(self, i):
        i += 1
        res = 0
        while (i > 0):
            res += self.bit[i]
            i -= i & -i
        return res
    
    def add(self, i, target):
        i += 1
        while i <= self.num:
            self.bit[i] += target
            i += i & -i
    
    # [l, r) 
    def query(self, l, r):
        return self.sum(r-1) - self.sum(l-1)

def main():
    N = int(input())
    S = list(input())
    Q = int(input())
    anss = []
    bits = [BinaryIndexedTree(N) for i in range(26)]

    for index, c in enumerate(S):
        bits[ord(c) - ord('a')].add(index, 1)
    
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            index = int(query[1]) - 1
            target = query[2]
            if S[index] == target:
                continue
            else:
                bits[ord(S[index])-ord('a')].add(index, -1)
                S[index] = target
                bits[ord(target)-ord('a')].add(index, 1)
        else:
            l, r = map(int, query[1:])
            l-= 1; r-= 1
            ans = 0
            for i in range(26):
                if bits[i].query(l, r+1) > 0:
                    ans += 1
            anss.append(ans)
    print(*anss, sep="\n")

if __name__ == "__main__":
    main()
