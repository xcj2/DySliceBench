import sys

def InputData():

    data_len = int(input())
    # data = input().split()
    data = list(map(int, input().split()))

    searchdata_len = int(input())
    # searchdata = input().split()
    searchdata = list(map(int, input().split()))

    # data = int(data)
    # searchdata = int(searchdata)

    return data_len, data, searchdata_len, searchdata

def Liner_Search(data, key):

    contained_cnt = 0
    # for i in range(searchdata_len):
    for i in range(len(data)):
        if key == data[i]:
            return 1
    
    # return contained_cnt
    return "NOT_FOUND"

def PrintOut(contained_cnt):
    print(int(contained_cnt))

def main():
    [data_len, data, searchdata_len, searchdata] = InputData()
    count = 0
    for i in searchdata:
        if Liner_Search(data, i)  != "NOT_FOUND":
            count += 1
    
    PrintOut(count)

if __name__=='__main__':
    main()
