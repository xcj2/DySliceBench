import sys
import math
import copy
from typing import Tuple, List, Union
input = sys.stdin.readline

class Area:
    def __init__(self, startidx: int, area: int):
        self.startidx = startidx
        self.area = area
    def __repr__(self):
        return "{}".format(self.area)


def main():
    edgeStack = []
    areaStack = []
    line = input()
    for idx, item in enumerate(line):
        if item is "\\":
            edgeStack.append(idx)
        elif item is "_":
            pass
        elif item is "/":
            if len(edgeStack) < 1:
                continue
            prevarea = 0
            previdx = edgeStack[-1]
            while (len(areaStack) > 0
                   and len(edgeStack) > 0
                   and areaStack[-1].startidx > edgeStack[-1]):
                area = areaStack.pop(-1)
                prevarea += area.area
            areaStack.append(Area(edgeStack.pop(-1), prevarea + idx - previdx))
    return areaStack


if __name__ == '__main__':
    areaStack = main()
    print(sum([area.area for area in areaStack]))
    if len(areaStack):
        print(len(areaStack), end=" ")
    else:
        print(len(areaStack), end="")
    print(" ".join([str(area) for area in areaStack]))

