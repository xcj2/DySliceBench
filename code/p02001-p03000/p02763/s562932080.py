
#bottom-up query
class SegmentTree():
    def __init__(self, num, segfunc, ide_ele):
        length = 2 ** (num-1).bit_length()
        self.n = num
        self.func = segfunc
        self.seg = [ide_ele] * 2 * length
        self.ide_ele = ide_ele
    
    def update(self, index, target):
        index += self.n - 1
        self.seg[index] = target
        while (index > 0):
            index = (index - 1) // 2
            self.seg[index] = self.func(self.seg[index*2 + 1], self.seg[index*2 + 2])
    
    # [l, r)
    def quary(self, l, r):
        l += self.n - 1
        r += self.n - 1
        res = self.ide_ele
        while l < r :
            if l & 1 == 0:
                res = self.func(res, self.seg[l])
            if r & 1 == 0:
                res = self.func(res, self.seg[r-1])
            l = l // 2
            r = (r-1) // 2
        return res

def main():
    N = int(input())
    S = list(input())
    Q = int(input())
    anss = []
    ide_ele = 10 ** 9
    segs = [SegmentTree(N, min, ide_ele) for i in range(26)]
    for index, c in enumerate(S):
        segs[ord(c) - ord('a')].update(index, index)
    
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            index = int(query[1]) - 1
            target = query[2]
            if S[index] == target:
                continue
            else:
                segs[ord(S[index])-ord('a')].update(index, ide_ele)
                S[index] = target
                segs[ord(target)-ord('a')].update(index, index)
        else:
            l, r = map(int, query[1:])
            l-= 1; r-= 1
            ans = 0
            for i in range(26):
                if segs[i].quary(l, r+1) <= r:
                    ans += 1
            anss.append(ans)
    print(*anss, sep="\n")

if __name__ == "__main__":
    main()
