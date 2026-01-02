import sys

input = sys.stdin.readline

class Dict:
    def __init__(self):
        self.table = [None] * 1046527
        self.table_size = 1046527
    
    def insert(self, key):
        colisions = 0
        while True:
            hash_num = self._calc_hash(self._to_num(key), colisions)
            cand = self.table[hash_num]
            if cand is None:
                self.table[hash_num] = key
                return 0
            elif cand == key:
                return 1
            colisions += 1
    
    def has(self, key):
        colisions = 0
        while True:
            hash_num = self._calc_hash(self._to_num(key), colisions)
            cand = self.table[hash_num]
            if cand == key:
                return True
            elif cand is None or colisions >= self.table_size:
                return False
            else:
                colisions += 1
        return 
    
    def _calc_hash(self, key, colisions):
        hash_1 = key % self.table_size
        hash_2 = 1 + (key % (self.table_size - 1))
        return (hash_1 + colisions * hash_2) % self.table_size
    
    def _to_num(self, str_key):
        sum = 0
        p = 1
        for char in str_key:
            if char == 'A':
                sum += 1 * p
            elif char == 'C':
                sum += 2 * p
            elif char == 'G':
                sum += 3 * p
            elif char == 'T':
                sum += 4 * p
            p *= 5
        return sum

def main_():
    N = int(input())
    commands = [(cmd[0], cmd[1]) for cmd in [input().split() for _ in range(N)]]
    hash_map = Dict()
    for cmd in commands:
        if cmd[0] == 'insert':
            hash_map.insert(cmd[1])
        else:
            ans = 'yes' if hash_map.has(cmd[1]) else 'no'
            print(ans)
            

if __name__ == "__main__":
    main_()

