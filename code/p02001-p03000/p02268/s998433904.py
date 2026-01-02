import sys
import math

def InputData():
    
    data_len = int(input())
    # data = int(input().split())
    data = list(map(int, input().split()))

    searchdata_len = int(input())
    # searchdata = int(input().split())
    searchdata = list(map(int, input().split()))
    # print([i for i in data])
    # print([i for i in searchdata])
    # print()
    # print(data_len)
    # print(searchdata_len)
    # print()

    # data = int(data)
    # searchdata = int(searchdata)

    return data_len, data, searchdata_len, searchdata

def Binary_Search(Data, key):
    
    right = len(Data)
    left = 0
    while left < right:
        mid = (left + right) // 2
        # print(searchdata[i])
        if key == Data[mid]:
            # print(searchdata[i])
            return mid
        elif key < Data[mid]:
            right = mid
        elif key > Data[mid]:
            left = mid + 1
        

    return "NOT_FOUND"

def PrintOut(count):
    print(count)

def main():
    [data_len, data, searchdata_len, searchdata] = InputData()
    count = 0
    for i in searchdata:
        if Binary_Search(data, i) != "NOT_FOUND":
            count += 1

    PrintOut(count)

if __name__=='__main__':
    main()
