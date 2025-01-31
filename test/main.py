import json

data = {
    'val1':0,
    'val2':0,
    'val3':0
}
tempData = {}

dataList = []

def setNewdata():
    newdata = data
    for ind in newdata:
        newdata[ind] = input(f'Inserisci {ind}: ')
    return newdata

def insertIndataList(data):
    dataList.append(data)
    print(dataList)


def getdata(dataList):
    for data in dataList:
        print(data)
        return(data)

def save(dataList):
    path = './test/mydata.json'
    with open(path, 'w') as fp:
        json.dump(dataList, fp, indent=2)

def initDataList():
    path = './test/mydata.json'
    with open(path, 'r') as rf:
        temp_data = json.load(rf)
    return temp_data

tempData = initDataList()
print(tempData)
insertIndataList(setNewdata())
save(dataList)

