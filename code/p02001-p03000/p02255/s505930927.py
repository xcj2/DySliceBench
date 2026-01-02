
def InsertionSort(data):
    show(data)
    for i in range(1, len(data)):
        temp = data[i]
        for j in reversed(range(0, i)):
            if data[j] > temp:
                data[j+1] = data[j]
            else:
                data[j+1] = temp
                break
            if j == 0:
                data[0] = temp
        show(data)
    return data

def Input():
    input()
    data = [int(e) for e in input().split()]
    return data

def show(data):
    string = str(data[0])
    for i in range(1, len(data)):
        string = string + " " + str(data[i])
    print(string)

InsertionSort(Input())
