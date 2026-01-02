def binary_search(array, tgt_no): #  arrayは昇順にソートされているものとする

    def compare_midpoint(tgt, array, start, end):
        midpoint = (end + start)//2
        if tgt == array[midpoint]:
            return True, None, None
        elif tgt < array[midpoint]:
            return False, start, midpoint
        elif tgt > array[midpoint]:
            return False, midpoint + 1, end

    start = 0
    end = len(array)
    while True:
        ret, start, end = compare_midpoint(tgt_no, array, start, end)
        if ret:
            return True
        if end <= start:
            return False


def main():
    _ = input()
    array_A = list(map(int, input().split()))
    _ = input()
    array_B = list(map(int, input().split()))

    cnt = 0
    for integer_B in array_B:
        if binary_search(array_A, integer_B):
            #print(integer_B)
            cnt += 1

    print(cnt)
    return


main()
