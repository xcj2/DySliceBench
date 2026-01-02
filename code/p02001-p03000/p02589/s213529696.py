
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

max2 = lambda x,y: x if x > y else y
min2 = lambda x,y: x if x < y else y

class TrieNode:
    def __init__(self, n_alphabets):
        self.children = [None]*n_alphabets
        self.end = False

class Trie:
    def __init__(self, n_alphabets):
        self.n_alphabets = n_alphabets
        self.root = TrieNode(n_alphabets)

    def add(self, s):
        n = self.root
        for c in s:
            if n.children[c] is None:
                n.children[c] = TrieNode(self.n_alphabets)
            n = n.children[c]
        n.end = True


def solve(L):
    L = [tuple(ord(c)-ord('a') for c in reversed(s)) for s in L]
    trie = Trie(26)

    for s in L:
        trie.add(s)
    
    cnt = 0
    for s in L:

        app = [0]*26
        for c in s:
            app[c] += 1

        node = trie.root
        for c in s:
            if node is None:
                break
            for d,n in enumerate(node.children):
                if n is not None and app[d] > 0 and n.end:
                    cnt += 1
            app[c] -= 1
            node = node.children[c]
    return cnt - len(L)




if __name__ == '__main__':
    N = int(readline())
    L = [s.decode().rstrip() for s in read().split()]
    print(solve(L))