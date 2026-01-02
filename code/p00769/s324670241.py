import sys
input = sys.stdin.readline

class Node():
    def __init__(self):
        self.is_leaf = False
        self.val = -1
        self.childs = []
        self.child_num = 0
        self.parent = None

    def win(self):
        if self.is_leaf:
            return self.val // 2 + 1
        tmp = []
        for c in self.childs:
            tmp.append(c.win())
        tmp = sorted(tmp)
        ret = 0
        for i in range(self.child_num//2 + 1):
            ret += tmp[i]
        return ret

def main():
    n = int(input())
    questions = [input().strip() for i in range(n)]

    for q in questions:
        root = Node()
        now = root
        i = 0
        while i < len(q):
            if q[i] == "[":
                tmp = Node()
                tmp.parent = now
                now.childs.append(tmp)
                now.child_num += 1
                now = tmp
                i += 1
            elif q[i] == "]":
                now = now.parent
                i += 1
            else:
                j = i
                while q[j+1] in "0123456789":
                    j += 1
                now.is_leaf = True
                now.val = int(q[i:j+1])
                i = j+1
        print(root.win())

if __name__ == "__main__":
    main()

