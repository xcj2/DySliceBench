class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.val = ''
    
    @classmethod
    def fromString(cls, s):
        pos = 1
        if s[pos] == '(':
            e = getEnd(s, 1)
            left = cls.fromString(s[1:e+1])
            pos = e + 2
        else:
            left = None
            pos += 1

        if s[pos] == '(':
            e = getEnd(s, pos)
            right = Node.fromString(s[pos:e+1])
        else:
            right = None

        return cls(left, right)

    def __str__(self):
        lstr = "" if self.left == None else str(self.left)
        rstr = "" if self.right == None else str(self.right)
        return "({},{})".format(lstr, rstr)

def getEnd(s, pos):
    count = 0
    while True:
        if s[pos] == '(':
            count += 1
        elif s[pos] == ')':
            count -= 1
        if count == 0:
            break
        pos += 1
    return pos

def intersection(root1, root2):
    if root1.left == None or root2.left == None:
        root1.left = None
    else:
        intersection(root1.left, root2.left)
    
    if root1.right == None or root2.right == None:
        root1.right = None
    else:
        intersection(root1.right, root2.right)

def union(root1, root2):
    if root1.left == None and root2.left == None:
        pass
    elif root1.left != None and root2.left == None:
        pass
    elif root1.left == None and root2.left != None:
        root1.left = root2.left
    else:
        union(root1.left, root2.left)
    
    if root1.right == None and root2.right == None:
        pass
    elif root1.right != None and root2.right == None:
        pass
    elif root1.right == None and root2.right != None:
        root1.right = root2.right
    else:
        union(root1.right, root2.right)

if __name__ == '__main__':
    try:
        while True:
            line = input().strip().split()
            c = line[0]
            a = Node.fromString(line[1])
            b = Node.fromString(line[2])

            if c == 'i':
                intersection(a, b)
            else:
                union(a, b)

            print(a)

    except EOFError:
        pass
