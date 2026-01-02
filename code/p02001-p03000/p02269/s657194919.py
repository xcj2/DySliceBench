class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class HashTable:
    def __init__(self, capacity):
        capacity = 2**capacity
        self.table = [None]*capacity
        self.mask = capacity - 1
    
    def insert(self, data):
        node = Node(data)
        remainder = hash(data) & self.mask
        node.next, self.table[remainder] = self.table[remainder], node
    
    def find(self, data):
        remainder = hash(data) & self.mask
        node = self.table[remainder]
        while node:
            if node.data == data:
                return True
            node = node.next
        return False      

    
if __name__ == "__main__":
    n = int(input())
    dictionary = HashTable(20)
    for _ in range(n):
        operation, string = input().split()
        if operation == "insert":
            dictionary.insert(string)
            continue
        print("yes" if dictionary.find(string) else "no")
