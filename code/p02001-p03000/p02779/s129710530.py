import hashlib
import math

class BloomFilter:

    def __init__(self, num_item, false_positive):
        assert 0 <= false_positive <= 1
        # Optimal number of bit array size and hash function
        # https://en.wikipedia.org/wiki/Bloom_filter#Optimal_number_of_hash_functions
        log2 = math.log(2)
        logp = math.log(false_positive)
        size = - num_item * logp / (log2 * log2)
        num_hash = size / num_item * log2

        self.size = int(math.ceil(size))
        self.num_hash = int(math.ceil(num_hash))

        self.array = self.BitArray(self.size)
        self.hash_functions = [self.HashFunction(i, self.size)
                               for i in range(self.num_hash)]

    def add(self, item):
        for hash_func in self.hash_functions:
            i = hash_func(item)
            self.array[i] = True

    def __contains__(self, item):
        return self.contains(item)

    def contains(self, item):
        for hash_func in self.hash_functions:
            i = hash_func(item)
            if self.array[i] is False:
                return False
        return True

    class BitArray:

        def __init__(self, length):
            # Allocate an object per a bit for simplicity
            self.array = [False for _ in range(length)]

        def __getitem__(self, index):
            return self.get(index)

        def get(self, index):
            return self.array[index]

        def __setitem__(self, index, bit):
            return self.set(index, bit)

        def set(self, index, bit):
            if bit > 0 or bit is True:
                self.array[index] = True
            else:
                self.array[index] = False

    class HashFunction:

        def __init__(self, seed, maximum):
            self.seed = seed.to_bytes(
                seed.bit_length() // 8 + 1, byteorder='big')
            self.maximum = maximum

        def __call__(self, byte_buffer):
            return self.call(byte_buffer)

        def call(self, byte_buffer):
            # MD5 is enough because I don't want to oneway hash function
            b = hashlib.md5(byte_buffer + self.seed).digest()
            i = int.from_bytes(b, byteorder='big', signed=False)
            return i % self.maximum

N = int(input())
L = list(map(int,input().split()))
bf = BloomFilter(num_item=5 * 10 ** 5, false_positive=0.001)

L = sorted(L)
for i in range(len(L) - 1):
    if L[i] == L[i+1]:
        print("NO")
        quit()
print("YES")
