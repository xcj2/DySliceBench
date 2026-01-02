class Node:
    def __init__(self, prev, val, next):
        self.prev = prev
        self.val = val
        self.next = next


NIL = 0
START = -1
END = -2


class List:
    def __init__(self, li):
        li.append(END)
        self.li = [Node(NIL, START, NIL)]
        for e in li:
            node = Node(self.li[-1], e, NIL)
            self.li[-1].next = node
            self.li.append(node)

        self.l = len(self.li) - 1
        self.ans = []

    def step(self):
        i = self.l
        u = self.li[-1]
        while u.val != START:
            if u.val == i:
                u.prev.next = u.next
                u.next.prev = u.prev
                self.ans.append(u.val)
                self.l -= 1
                return True

            else:
                u = u.prev
                i -= 1

        self.ans = [-1]
        return False

    def solve(self):
        for _ in range(self.l - 1):
            if not self.step():
                break

        print(*self.ans[::-1], sep="\n")


def main():
    n = int(input())
    b = list(map(int, input().split()))

    l = List(b)
    l.solve()


if __name__ == "__main__":
    main()
