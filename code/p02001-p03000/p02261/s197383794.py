import sys
import copy

def print_data(data):
    last_index = len(data) - 1
    
    for idx, item in enumerate(data):
        print(item, end='')
        if idx != last_index:
            print(' ', end='')

    print('')

def bubbleSort(data, N):
    for i in range(N):
        j = N -1
        while j >= i+1:
            if data[j][1] < data[j-1][1]:
                hoge = data[j]
                data[j] = data[j-1]
                data[j-1] = hoge
            j -= 1
    return data

def selectSort(data, N):
    for i in range(N):
        mini = i
        for j in range(i, N):
            if data[j][1] < data[mini][1]:
                mini = j
        if i == mini:
            pass
        else:
            hoge = data[mini]
            data[mini] = data[i]
            data[i] = hoge
    
    return data

def isStable(inData, outData, N):
    for i in range(N):
        for j in range(i+1, N):
            if inData[i][1] == inData[j][1]:
                a = outData.index(inData[i])
                b = outData.index(inData[j])
                if a > b :
                    return False
    return True




def main():
    N = int(input())
    data0 = list(input().split())
    data1 = copy.deepcopy(data0)
    data2 = copy.deepcopy(data0)
    
    bubbleData = bubbleSort(data1, N)
    selectData = selectSort(data2, N)
    
    
                  
        
    print_data(bubbleData)
    if isStable(data0, bubbleData, N):
        print('Stable')
    else:
        print('Not stable')
    
        
    print_data(selectData)
    if isStable(data0, selectData, N):
        print('Stable')
    else:
        print('Not stable')

            
if __name__ == '__main__':
    main()
