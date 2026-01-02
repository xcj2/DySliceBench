from random import randint
# from typing import TypeVar, Tuple, List, Optional, Iterable


# K = TypeVar("K")
# V = TypeVar("V")

class ListNode:
    def __init__(self, key, value, next_=None):
        self.key, self.value, self.next = key, value, next_


class HashMapLinkedList:
    def __init__(self):
        self.__head = ListNode(None, None)
        self.__tail = self.__head
        self.__num_items = 0

    def __repr__(self):
        return "->" +  " -> ".join(str(kv_pair) for kv_pair in self)

    def __len__(self):
        return self.__num_items

    def find(self, key):
        cur_node = self.__head.next
        while cur_node:
            if cur_node.key == key:
                return cur_node
            cur_node = cur_node.next
        raise ValueError(key if type(key) != str else "'" + key + "'")

    def insert(self, key, value):
        # when there already exists the key-value pair, update the value.
        try:
            node = self.find(key)
            node.value = value
            return 0
        # Otherwise, add a new key-value pair.
        except ValueError:
            self.__tail.next = ListNode(key, value)
            self.__tail = self.__tail.next
            self.__num_items += 1
            return 1

    def delete(self, key):
        cur_node = self.__head
        while cur_node.next:
            if cur_node.next.key == key:
                cur_node.next = cur_node.next.next
                self.__num_items -= 1
                return
            cur_node = cur_node.next

    def __iter__(self):
        self._cur_node = self.__head.next
        return self

    def __next__(self):
        if not self._cur_node:
            raise StopIteration()
        key, value = self._cur_node.key, self._cur_node.value
        self._cur_node = self._cur_node.next
        return (key, value)


class HashMap:
    SCALE_FACTOR = 2
    SHRINKAGE_THRESHOLD = 4
    PRIME_NUMBER = (1 << 31) - 1
    def __init__(self, capacity=16):
        self.__arr = [HashMapLinkedList() for _ in range(capacity)]
        self.__capacity = capacity
        self.__num_items = 0
        self.__param1 = randint(0, self.PRIME_NUMBER - 1)
        self.__param2 = randint(0, self.PRIME_NUMBER - 1)

    def __repr__(self) -> str:
        kv_pairs = [kv_pair for linked_list in self.__arr for kv_pair in linked_list]
        return "{" + ", ".join((str(key) if type(key) != str else "'" + key + "'") \
            + ": " + str(value) for key, value in kv_pairs) + "}"

    def __len__(self) -> int:
        return self.__num_items

    def _range_hash(self, prehash):
        """
        Converts an arbitrary integer to an integer within [0, self.__capacity).
        """
        return (self.__param1 * prehash + self.__param2) % self.__capacity
    
    def _resize(self, enlarge=True):
        if enlarge:
            self.__capacity *= self.SCALE_FACTOR
        else:
            self.__capacity //= self.SCALE_FACTOR
        new_arr = [HashMapLinkedList() for _ in range(self.__capacity)]
        for linked_list in self.__arr:
            for key, value in linked_list:
                new_idx = self._range_hash(hash(key))
                new_arr[new_idx].insert(key, value)
        self.__arr = new_arr

    def insert(self, key, value):
        """
        Inserts an item whose key and value are key and value.
        """
        idx = self._range_hash(hash(key))
        self.__num_items += self.__arr[idx].insert(key, value)
        # When #items becomes the capacity, double the capacity.
        if self.__num_items == self.__capacity:
            self._resize(enlarge=True)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def find(self, key):
        """
        Find the corresponding value given a key.
        """
        idx = self._range_hash(hash(key))
        node = self.__arr[idx].find(key)
        return node.value

    def __getitem__(self, key):
        return self.find(key)
    
    def __contains__(self, key):
        try:
            self.find(key)
            return True
        except ValueError:
            return False

    def delete(self, key):
        """
        Delete the item whose key is key.
        """
        idx = self._range_hash(hash(key))
        self.__arr[idx].delete(key)
        self.__num_items -= 1
        # When #items is less than or equal to the capacity, halve the capacity.
        if self.__num_items * self.SHRINKAGE_THRESHOLD <= self.__capacity:
            self._resize(enlarge=False)

    def __delitem__(self, key):
        self.delete(key)
    
    def keys(self):
        for linked_list in self.__arr:
            for k, _ in linked_list:
                yield k
    
    def values(self):
        for linked_list in self.__arr:
            for _, v in linked_list:
                yield v
    
    def items(self):
        for linked_list in self.__arr:
            for k, v in linked_list:
                yield (k, v)


N = int(input())
counter = HashMap()

for _ in range(N):
    s = input()
    if s not in counter:
        counter[s] = 1
    else:
        counter[s] += 1

M = int(input())
for _ in range(M):
    s = input()
    if s in counter:
        counter[s] -= 1

max_profit = 0
for profit in counter.values():
    max_profit = max(max_profit, profit)
print(max_profit)