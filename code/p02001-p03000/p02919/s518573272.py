from operator import itemgetter


class RedBlackTree:
    # For performance, nodes are implemented as lists.
    #   [left, right, data, color, count]
    #   color: 1:RED  0:BLACK
    #
    # It is useful to set the left/right index to 0/1 for boolean access.
    #
    # The end nodes are BLACK and of which value is EOT (End Of Tree).

    def __init__(self, EOT=-1):
        self.EOT = EOT
        self.root = self._leaf()

    def _leaf(self):
        return [None, None, self.EOT, 0, 0]

    def _rotate(self, node, r):
        child = node[r ^ 1]
        node[r ^ 1] = child[r]
        child[r] = node
        child[3] = node[3]
        node[3] = 1
        child_count = child[4]
        child[4] = node[4]
        node[4] -= child_count - node[r ^ 1][4]
        return child

    def insert(self, x):
        stack = []
        node = self.root
        while node[2] != self.EOT:
            # Variation: If the same value is not allowed, return when found.

            to_right = x >= node[2]
            stack.append((node, to_right))
            node = node[to_right]

        # Insert values to the end node
        node[0] = self._leaf()
        node[1] = self._leaf()
        node[2] = x
        node[3] = 1
        node[4] = 1

        # Increase count
        for parent, _ in stack:
            parent[4] += 1

        # Validate tree and rotate if needed.
        while stack:
            parent, r = stack.pop()
            if parent[3] == 1:
                node = parent
                continue
            parent[r] = node
            node, flag = self._balance_insert(parent, r)

            if stack and flag == True:
                parent, r = stack.pop()
                parent[r] = node
                break

        else:
            # If the root might have changed, update its color.
            self.root = node
            self.root[3] = 0

    def _balance_insert(self, node, r):
        flag = True
        if node[r][r ^ 1][3] == 1:
            node[r] = self._rotate(node[r], r)
        if node[r][r][3] == 1:
            if node[r ^ 1][3] == 1:
                node[3] = 1
                node[r ^ 1][3] = node[r][3] = 0
                flag = False
            else:
                node = self._rotate(node, r ^ 1)
        return node, flag

    def delete(self, x):
        node = self.root
        stack = []
        while node[2] != x:
            r = node[2] < x
            stack.append((node, r))
            node = node[r]

        # Not Found
        if node[2] == self.EOT:
            return

        # Node has 2 children: swap min node in right tree and delete min node
        if node[0][2] != self.EOT and node[1][2] != self.EOT:
            stack.append((node, 1))
            min_node = self.get_min(node[1], stack)
            node[2] = min_node[2]
            node = min_node

        # Decrease count
        for parent, _ in stack:
            parent[4] -= 1

        # Node has 0/1 child
        parent, r = stack[-1]
        if node[0][2] == self.EOT:
            parent[r] = node[1]
            node[1][3] = 0
            # Balance is only needed if both children are EOT and self color is black.
            if node[1][2] != self.EOT or node[3] == 1:
                return
        elif node[1][2] == self.EOT:
            parent[r] = node[0]
            node[0][3] = 0
            return

        # Validate tree and rotate if needed.
        while stack:
            parent, r = stack.pop()
            node, flag = self._balance_delete(parent, r)

            if stack and flag == True:
                parent, r = stack.pop()
                parent[r] = node
                break
        else:
            # If the root might have changed, update its color.
            self.root = node
            self.root[3] = 0

    def get_min(self, node, stack):
        while node[0][2] != self.EOT:
            stack.append((node, 0))
            node = node[0]
        return node

    def _balance_delete(self, node, r):
        if node[r ^ 1][r][3] == 0 and node[r ^ 1][r ^ 1][3] == 0:
            if node[r ^ 1][3] == 0:
                node[r ^ 1][3] = 1
                if node[3] == 0:
                    return node, False
                node[3] = 0
            else:
                node = self._rotate(node, r)
                node[r], _ = self._balance_delete(node[r], r)
        else:
            if node[r ^ 1][r][3] == 1:
                node[r ^ 1] = self._rotate(node[r ^ 1], r ^ 1)
            node = self._rotate(node, r)
            node[r][3] = 0
            node[r ^ 1][3] = 0
        return node, True

    def upper_bound(self, x):
        """
        :return Smallest y satisfying x < y and its leftmost index.
                If not exists, (EOT, length) will be returned.
        """
        node = self.root
        y = self.EOT
        i = node[4]
        j = 0
        while node[2] != self.EOT:
            if x < node[2]:
                y = node[2]
                i = j + node[0][4]
                node = node[0]
            else:
                j += node[0][4] + 1
                node = node[1]
        return y, i

    def lower_bound(self, x):
        """
        :return Smallest y satisfying x <= y and its leftmost index.
                If not exists, (EOT, length) will be returned.
        """
        node = self.root
        y = self.EOT
        i = node[4]
        j = 0
        while node[2] != self.EOT:
            if x <= node[2]:
                y = node[2]
                i = j + node[0][4]
                node = node[0]
            else:
                j += node[0][4] + 1
                node = node[1]
        return y, i

    def get_by_index(self, i):
        """
        :return (0-indexed) i-th smallest item.
                If i is greater than length, EOT will be returned.
        """
        node = self.root
        if node[4] <= i:
            return self.EOT
        j = i
        while node[2] != self.EOT:
            left_count = node[0][4]
            if left_count == j:
                return node[2]
            elif left_count > j:
                node = node[0]
            else:
                j -= left_count + 1
                node = node[1]

    def debug_print(self):
        self._debug_print(self.root, 0)

    def _debug_print(self, node, depth):
        if node[2] != self.EOT:
            self._debug_print(node[0], depth + 1)
            print('      ' * depth, 'BR'[node[3]], node[2], node[4])
            self._debug_print(node[1], depth + 1)


n = int(input())
ppp = list(map(int, input().split()))
pps = list(enumerate(ppp))
pps.sort(reverse=True, key=itemgetter(1))

rbt = RedBlackTree(-2)
rbt.insert(-1)
rbt.insert(-1)
rbt.insert(n)
rbt.insert(n)

ans = 0
for i, p in pps:
    r1, j = rbt.upper_bound(i)
    r2 = rbt.get_by_index(j + 1)
    l1 = rbt.get_by_index(j - 1)
    l2 = rbt.get_by_index(j - 2)
    ans += p * ((l1 - l2) * (r1 - i) + (r2 - r1) * (i - l1))
    rbt.insert(i)
print(ans)
