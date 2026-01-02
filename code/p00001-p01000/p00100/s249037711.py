# coding: utf-8
# Here your code !
employeeSalesList = []

def resetDataset():
    del employeeSalesList[0 : len(employeeSalesList) + 1]

def readDataCount():
    return int(input())

def searchEmployeeSales(employeeId):
    for data in employeeSalesList:
        if data[0] == employeeId:
            return data
    
    newData = [employeeId, 0]
    employeeSalesList.append(newData)
    return newData

def checkSales():
    employeeId, price, volume = list(map(int, input().split(" ")))
    employeeSales = searchEmployeeSales(employeeId)
    employeeSales[1] += price * volume

answerList = []
def printEmployeeOfDataset():
    found = False
    for data in employeeSalesList:
        if data[1] >= 1000000:
            answerList.append(data[0])
            found = True
    if not found:
        answerList.append("NA")

resetDataset()
dataCount = readDataCount()
while dataCount > 0:
    for _ in range(dataCount):
        checkSales()
    printEmployeeOfDataset()
    resetDataset()
    dataCount = readDataCount()

for row in answerList:
    print(row)