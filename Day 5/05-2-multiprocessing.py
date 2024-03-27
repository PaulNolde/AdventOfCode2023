from multiprocessing import Process, Manager

##################################
#nicht zu empfehlen, Laufzeit weit über 1h!
##################################

def part2(categories):
   with Manager() as manager:
        results = manager.list()
        processes = []
        groupSize = 10000000

        for seedGroups in range(int(len(categories[0][0])/2)):
            sg = [categories[0][0][2*seedGroups], categories[0][0][2*seedGroups+1]]
            while sg[1] > 0:
                if sg[1] > groupSize:
                    process = Process(target=seedGroup, args=(sg[0], groupSize, results, categories))
                    processes.append(process)
                    process.start()
                    sg[0] += groupSize
                    sg[1] -= groupSize
                else:
                    process = Process(target=seedGroup, args=(sg[0], sg[1], results, categories))
                    processes.append(process)
                    process.start()
                    sg[1] = 0
        for process in processes:
            process.join()

        print(results)
        print(min(results))   

        
def seedGroup(start, length, results, categories):
    print("seed group: " + str(start)+ " to " + str(start + length - 1))
    minLocation = float('inf')
    for seed in range(start, start + length ):
        number = seed
        for c in range(1, len(categories)):
            for map in categories[c]:
                #print(number, map)
                if map[1] <= number < map[1] + map[2]:
                    number = map[0] + (number-map[1])
                    break

        if number < minLocation:
            minLocation = number

    results.append(minLocation)
        
    print(minLocation)
    return minLocation

if __name__ == '__main__':

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
    part2(categories)
