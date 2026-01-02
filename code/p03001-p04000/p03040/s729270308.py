from heapq import *

def main():
    from sys import stdin, stdout

    def read():
        return stdin.readline().rstrip('\n')

    def read_array(sep=None, maxsplit=-1):
        return read().split(sep, maxsplit)

    def read_int():
        return int(read())

    def read_int_array(sep=None, maxsplit=-1):
        return [int(a) for a in read_array(sep, maxsplit)]

    def write(*args, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join(str(a) for a in args) + end)

    def write_array(array, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join(str(a) for a in array) + end)

    lower_heap = []
    higher_heap = []
    median = constant = sum_lower = sum_higher = 0
    for _ in range(read_int()):
        ar = read_int_array()
        if len(ar) == 3:
            constant += ar[2]
            x = ar[1]
            if not lower_heap:
                lower_heap.append(-x)
                sum_lower += x
                median = x
            elif not higher_heap:
                heappush(lower_heap, -x)
                sum_lower += x

                x = -heappop(lower_heap)
                sum_lower -= x
                heappush(higher_heap, x)
                sum_higher += x
                median = -lower_heap[0]
            elif x <= -lower_heap[0]:
                heappush(lower_heap, -x)
                sum_lower += x

                if len(lower_heap) - len(higher_heap) > 1:
                    x = -heappop(lower_heap)
                    sum_lower -= x
                    heappush(higher_heap, x)
                    sum_higher += x
                median = -lower_heap[0]
            else:
                heappush(higher_heap, x)
                sum_higher += x
                if len(higher_heap) > len(lower_heap):
                    x = heappop(higher_heap)
                    sum_higher -= x
                    heappush(lower_heap, -x)
                    sum_lower += x
                median = -lower_heap[0]
        else:
            write(median, constant + abs(sum_lower - median * len(lower_heap)) + abs(sum_higher - median * len(higher_heap)))
main()
