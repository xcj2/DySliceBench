import sys
from random import randint
# from typing import TypeVar, Tuple, List
finput = sys.stdin.readline



# K = TypeVar("K")

class ListNode:
    def __init__(self, key, next_=None):
        self.key, self.next = key, next_


class HashSetLinkedList:
    def __init__(self):
        self.__head = ListNode(None)
        self.__tail = self.__head
    
    def __repr__(self):
        keys = [str(key) if type(key) != str else "'" + key + "'" for key in self]
        return "->" + " -> ".join(keys)

    def find(self, key):
        cur_node = self.__head.next
        while cur_node:
            if cur_node.key == key:
                return True
            cur_node = cur_node.next
        return False

    def insert(self, key):
        if not self.find(key):
            self.__tail.next = ListNode(key)
            self.__tail = self.__tail.next
            return 1
        return 0

    def delete(self, key):
        cur_node = self.__head
        while cur_node.next:
            if cur_node.next.key == key:
                cur_node.next = cur_node.next.next
                return
            cur_node = cur_node.next

    def __iter__(self):
        self._cur_node = self.__head.next
        return self

    def __next__(self):
        if not self._cur_node:
            raise StopIteration()
        key = self._cur_node.key
        self._cur_node = self._cur_node.next
        return key


class HashSet:
    SCALE_FACTOR = 2
    SHRINKAGE_THRESHOLD = 4
    PRIME_NUMBER = (1 << 31) - 1
    def __init__(self, capacity=16):
        self.__arr = [HashSetLinkedList() for _ in range(capacity)]
        self.__capacity = capacity
        self.__num_items = 0
        self.__param1, self.__param2 = randint(0, self.PRIME_NUMBER - 1), randint(0,self.PRIME_NUMBER - 1)
    
    def __repr__(self):
        return "{" + ", ".join((str(key) if type(key) != str else "'" + key + "'") \
            for linked_list in self.__arr for key in linked_list) + "}"

    def __len__(self):
        return self.__num_items

    def _range_hash(self, prehashed_key):
        return (self.__param1 * prehashed_key + self.__param2) % self.__capacity

    def _resize(self, enlarge=True):
        if enlarge:
            self.__capacity *= self.SCALE_FACTOR
        else:
            self.__capacity //= self.SCALE_FACTOR
        new_arr = [HashSetLinkedList() for _ in range(self.__capacity)]
        for linked_list in self.__arr:
            for key in linked_list:
                new_idx = self._range_hash(hash(key))
                new_arr[new_idx].insert(key)
        self.__arr = new_arr

    def add(self, key):
        idx = self._range_hash(hash(key))
        self.__num_items += self.__arr[idx].insert(key)
        # Double the capacity.
        if self.__num_items == self.__capacity:
            self._resize(enlarge=True)

    def find(self, key):
        idx = self._range_hash(hash(key))
        return self.__arr[idx].find(key)

    def __contains__(self, key):
        return self.find(key)

    def discard(self, key):
        idx = self._range_hash(hash(key))
        self.__arr[idx].delete(key)
        self.__num_items -= 1
        # Halve the capacity when #items is less than or equal to 
        # the capacity / SHRINKAGE_THRESHOLD.
        if self.__num_items * self.SHRINKAGE_THRESHOLD <= self.__capacity:
            self._resize(enlarge=False)


N = int(finput())
d_list = [int(finput()) for _ in range(N)]

d_set = HashSet()
for d in d_list:
    d_set.add(d)

# d_set = set(d_list)
print(len(d_set))
