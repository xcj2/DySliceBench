class SegmentTree():
    def __init__(self, size):
        self.size = 2**((size-1).bit_length())
        self.val = [0]*(self.size*2)
    
    def update(self, i, x):
        i += self.size
        self.val[i] = x
        
        while i > 0:
            i = i >> 1
            self.val[i] = self.val[2*i] + self.val[2*i+1]
    
    def query(self, l, r):
        l += self.size
        r += self.size

        l_sum = 0
        r_sum = 0

        while l < r:
            if l & 1:
                l_sum += self.val[l]
                l += 1
            l = l >> 1

            if r & 1:
                r -= 1
                r_sum += self.val[r]
            r = r >> 1

        return l_sum + r_sum

def convertAlphabetToNumber(s):
    return ord(s) - ord('a')

N = int(input())
S = input()
Q = int(input())
query = [input().split() for i in range(Q)]

for i in range(Q):
    query[i][0] = int(query[i][0])
    query[i][1] = int(query[i][1]) - 1
    if query[i][0] == 2:
        query[i][2] = int(query[i][2]) - 1

alphabet_position = [SegmentTree(N) for i in range(28)]

for i in range(N):
    num = convertAlphabetToNumber(S[i])
    alphabet_position[num].update(i, 1)

for i in range(Q):
    if query[i][0] == 1:
        for j in range(28):
            if j == convertAlphabetToNumber(query[i][2]):
                alphabet_position[j].update(query[i][1], 1)
            else:
                alphabet_position[j].update(query[i][1], 0)
    else:
        cnt = 0
        for j in range(28):
            if alphabet_position[j].query(query[i][1], query[i][2] + 1) > 0:
                cnt += 1
        print(cnt)