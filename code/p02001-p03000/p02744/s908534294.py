def main():
    class Node:
        __slots__ = ["string", "index"]
        def __init__(self, string, index):
            self.string = string
            self.index = index

        def get_children(self):
            parent = self.string
            out = [None]*(self.index+1)
            for i, c in enumerate(s[:self.index]):
                out[i] = Node(parent+c, self.index)
            out[i+1] = Node(parent+s[self.index], self.index+1)
            return out

    n = int(input())
    root = Node("a", 1)
    children = [root]
    for _ in range(n-1):
        parents, children = children, []
        for parent in parents:
            children.extend(parent.get_children())
    for child in children:
        print(child.string)

if __name__ == "__main__":
    s = "abcdefghij"
    main()