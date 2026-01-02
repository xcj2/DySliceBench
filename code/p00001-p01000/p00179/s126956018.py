from copy import deepcopy
from collections import deque


class Bug:
    __convert = {"r": 1, "g": 2, "b": 3}
    __weight = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

    def __init__(self, state, time):
        self.state = list(state)
        self.time = time

    def color_change(self):
        box = []

        for item1, item2, index in zip(self.state[:-1], self.state[1:], range(len(self.state))):
            if item1 != item2:

                if item1 == "r" and item2 == "g" or item1 == "g" and item2 == "r":
                    color = "b"
                elif item1 == "r" and item2 == "b" or item1 == "b" and item2 == "r":
                    color = "g"
                else:
                    color = "r"

                copy_state = deepcopy(self.state)

                copy_state[index] = color
                copy_state[index + 1] = color

                box.append(copy_state)

        return box

    def is_same_color(self):
        first = self.state[0]
        return all([item == first for item in self.state])

    def __hash__(self):
        tmp = [self.__convert[item] * w for item, w in zip(self.state, self.__weight)]
        return sum(tmp)

    def __eq__(self, other):
        return all([item1 == item2 for item1, item2 in zip(self.state, other.state)])


while True:

    input_data = input()

    if input_data[0] == "0":
        break

    state_queue = deque()
    pattern = set()

    first = Bug(input_data, 0)

    if first.is_same_color():
        answer = 0
    else:
        answer = "NA"
        state_queue.appendleft(first)
        pattern.add(first)

    while len(state_queue) != 0:

        original = state_queue.pop()
        boxes = original.color_change()

        for state in boxes:

            item = Bug(state, original.time + 1)

            if item.is_same_color():
                answer = item.time

                state_queue.clear()
                break
            else:
                if item not in pattern:
                    pattern.add(item)
                    state_queue.appendleft(item)

    print(answer)

