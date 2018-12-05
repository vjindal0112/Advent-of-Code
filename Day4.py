f = open("Inputs//Day4.txt")

data = []


for line in f:
    data.append(line)

def sort(start, end):
    for x in range(len(data)):
        min = 15
        minIndex = -1
        for y in range(x, len(data)):
            temp = int(data[x][start:end])
            if(temp < min):
                min = temp
                minIndex = y

        tempFirstEntry = data[x]
        tempSwitcherooEntry = data[minIndex]
        data[minIndex] = tempFirstEntry
        data[x] = tempSwitcherooEntry


sort(6,8)

for line in data:
    print(line)
