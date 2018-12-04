f = open("Inputs//Day3.txt", 'r')

data = []
sqFeet = 0

for line in f:
    data.append(line)

xs = []
ys = []
widths = []
heights = []
ids = []

for line in data:
    xs.append(int(line[line.index('@') + 2: line.index(',')]))
    ys.append(int(line[line.index(',') + 1: line.index(':')]))
    widths.append(int(line[line.index(':') + 2: line.index('x')]))
    heights.append(int(line[line.index('x') + 1: len(line)]))
    ids.append(int(line[1: line.index('@') - 1]))

# Find necessary size of array
greatestx = 0
greatestxIndex = 0
for num in range(len(xs)):
    if(xs[num] > greatestx):
        greatestx = xs[num]
        greatestxIndex = num

greatesty = 0
greatestyIndex = 0
for num in range(len(ys)):
    if(ys[num] > greatesty):
        greatesty = ys[num]
        greatestyIndex = num


maxWidth = widths[greatestxIndex] + greatestx  + 2# make sure this isn't 1 off or something
maxHeight = heights[greatestyIndex] + greatesty + 2

field = [[0 for y in range(maxWidth)] for x in range(maxHeight)]
goldenIndex = 0
for index in range(len(data)):
    happened = False
    for x in range(xs[index], xs[index] + widths[index]):
        for y in range(ys[index], ys[index] + heights[index]):
            field[x][y] += 1

for x in range(len(field)):
    for y in range(len(field[0])):
        if(field[x][y] >=2):
            sqFeet += 1

# Part 2
for index in range(len(data)):
    happened = False
    for x in range(xs[index], xs[index] + widths[index]):
        for y in range(ys[index], ys[index] + heights[index]):
            if(field[x][y] > 1):
                happened = True
    if(not happened):
        goldenIndex = index

print(sqFeet)
print(ids[goldenIndex])
