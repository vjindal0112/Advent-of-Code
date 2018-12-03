f = open("Inputs//Day1.txt", 'r')

nums = set([0])
num = 0
count = 0

data = []

for line in f:
    data.append(int(line))

while(True):
    for datum in data:
        num += datum
        found = False;
        if num in nums:
            found = True
            break
        nums.add(num)
    if(found):
        break

print("HERE IT IS:")
print(num)
