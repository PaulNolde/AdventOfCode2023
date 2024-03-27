import timeit
file1 = open('input.txt', 'r')
Lines = file1.readlines()

categories = []
currCategory =[]
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

def intersect(interval1, interval2):
    start1, length1 = interval1[0], interval1[1]
    start2, length2 = interval2[0], interval2[1]
    end1 = start1 + length1
    end2 = start2 + length2

    iStart = max(start1, start2)
    iEnd = min(end1, end2)

    iLength = max(0, min(length1, length2, iEnd - iStart))
    if iLength > 0:
        return [iStart, iLength]
    return []

def remainingInterval(interval, intersec):
    start1, length1 = interval[0], interval[1]
    start2, length2 = intersec[0], intersec[1]

    end1 = start1 + length1
    end2 = start2 + length2

    if start1 < start2:
        restBefore = [start1, start2-start1]
    else:
        restBefore = None
    
    if end2 < end1:
        restAfter = [end2, end1 - end2]
    else:
        restAfter = None

    return restBefore, restAfter

def part2():
    minLocation = float('inf')
    intervalQueue = []
    for seedGroup in range(int(len(categories[0][0])/2)):
        intervalQueue = [[categories[0][0][2*seedGroup], categories[0][0][2*seedGroup+1]]]
        for c in range(1, len(categories)):
            nextStage = []
            while intervalQueue:
                currInterval = intervalQueue.pop(0)
                mapFlag = False
                for map in categories[c]:
                    mapInterval = [map[1], map[2]]
                    inter = intersect(mapInterval, currInterval)
                    mappedInter = []
                    before, after = [], []
                    if(inter):
                        before, after = remainingInterval(currInterval, inter)
                        if before:
                            intervalQueue.append(before)
                        if after:
                            intervalQueue.append(after)
                        mappedInter = [inter[0] + (map[0] -map[1]), inter[1]]
                        nextStage.append(mappedInter)
                        mapFlag = True
                        break
                if not mapFlag:
                    nextStage.append(currInterval)
            intervalQueue = nextStage
        minGroup = min(nextStage, key=lambda x: x[0])
        minLocation = min(minLocation, minGroup[0])
    print(minLocation)   

part2()
# execution_time = timeit.timeit(part2, number=100)
# print(f"Average execution time: {execution_time / 100} seconds")