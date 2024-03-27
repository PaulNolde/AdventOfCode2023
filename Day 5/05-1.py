import timeit
file1 = open('input.txt', 'r')
Lines = file1.readlines()

categories = []
currCategory =[]
# for i in range(len(Lines)):
for line in Lines:
    try:
        newLine = list(map(int, line.strip().split()))
    except ValueError:
        newLine = None

    if currCategory and (newLine == None or newLine == []):
        categories.append(currCategory)
        currCategory = []
    elif(newLine != None and newLine != []):
        currCategory.append(newLine)
categories.append(currCategory)



def part1():
    minLocation = float('inf')
    locations = []
    for seed in categories[0][0]:
        number = seed
        for c in range(1, len(categories)):
            for map in categories[c]:
                #print(number, map)
                if map[1] <= number < map[1] + map[2]:
                    number = map[0] + (number-map[1])
                    break
        locations.append(number)
        if number < minLocation:
            minLocation = number
    print(minLocation)

                

part1()
# execution_time = timeit.timeit(part1, number=100)
# print(f"Average execution time: {execution_time / 100} seconds")