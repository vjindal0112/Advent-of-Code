# PART 1

# f = open("Day2.txt", 'r')
#
# twoCount = 0
# threeCount = 0
#
# for line in f:
#     letters = []
#     for letter in line:
#         letters.append(letter)
#     three = False
#     two = False
#     for x in range(len(letters)):
#         print("x: " + str(x))
#         count = 0
#         for y in range(letters.index(letters[x]), len(letters)):
#             print("y: " + str(y))
#             if(letters[x] == letters[y]):
#                 count += 1
#         if(count == 3):
#             three = True
#         if(count == 2):
#             two = True
#     if(three):
#         threeCount += 1
#     if(two):
#         twoCount += 1
#
# print(twoCount)
# print(threeCount)
# print(twoCount * threeCount)


# PART 2

f = open("Day2.txt", 'r')

data = []

for line in f:
    data.append(line)

line1 = ""
line2 = ""
found = False
for x in range(len(data)):
    line1 = data[x]
    letters = []
    for letter in data[x]:
        letters.append(letter)
    for y in range(x+1, len(data)):
        line2 = data[y]
        count = 0
        for index in range(len(data[y])):
            if (data[y][index] != letters[index]):
                count += 1
            if(count > 1):
                break;
        if (count == 1):
            found = True
            break
    if found:
        break;


print(line1)
print(line2)
