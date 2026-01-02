from sys import stdin

class BIT:
    def __init__(self, n):
        self.data = [0] * (n + 10)
        
    def upd(self, pos, val = 1):
        pos += 1
        while pos < len(self.data):
            self.data[pos] += val
            pos += pos & -pos
            
    def get(self, pos):
        ans = 0
        pos += 1
        while pos > 0:
            ans += self.data[pos]
            pos -= pos & -pos
        return ans
    
    def get_range(self, l, r):
        return self.get(r) - self.get(l - 1)

def main():
    n, q = map(int, stdin.readline().split())
    color = list(map(int, stdin.readline().split()))
    
    queries = []
    for i in range(q):
        l, r = map(int, stdin.readline().split())
        queries.append((l, r, i))
    queries.sort(key = lambda val: val[1])
    
    ans = [0] * q
    prev_pos = [0] * (n + 1)
    bit = BIT(n + 1)
    
    f = 0
    for cur_pos, color in enumerate(color, 1):
        bit.upd(prev_pos[color], -1)
        bit.upd(cur_pos, 1)
        prev_pos[color] = cur_pos
        
        while f < q and queries[f][1] == cur_pos:
            ans[queries[f][2]] = bit.get_range(queries[f][0], queries[f][1])
            f += 1
    print('\n'.join(map(str, ans)))
    
main()
