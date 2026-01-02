#!/usr/bin/python
#-- coding=utf8



def exchangeData(A, it1, it2):
    tmp = A[it1]
    A[it1] = A[it2]
    A[it2] = tmp


def partition(A, p, r):
    x=A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            exchangeData(A, i, j)

    exchangeData(A, i+1, r)
    return i+1


def print_partitionData(A, part_index):
    for i, s in enumerate(A):
        if i !=0:
            print(" ", end= "")

        if i==part_index :
            print ("[{}]".format( s), end="")
        else:
            print (s, end="")
    print("")

        
def inputData():
    data = map(int, input().split())
    return list(data)

if __name__ == "__main__" :
    input()
    A = inputData()
    part_index = partition(A, 0, len(A)-1)
    print_partitionData(A, part_index)


