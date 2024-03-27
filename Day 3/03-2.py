from collections import defaultdict

file1 = open('input.txt', 'r')
Lines = file1.readlines()

def isGear(x):
    if x == '*':
        return 1
    else:
        return 0
    
cols = len(Lines[0])-1
rows = len(Lines)

schematic = [['0' for _ in range(cols)] for _ in range(rows)]
for row in range(len(Lines)):
    for col, c in enumerate(Lines[row][0:len(Lines[0])-1]):
        schematic[row][col] = c

     



def validPosition(y, x):
    return 0 <= y < rows and 0 <= x < cols

def isSymbolAdjacent(y, x):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dx, dy in directions:
        if validPosition(y+dy, x+dx) and isGear(schematic[y+dy][x+dx]):
            return [True, y+dy, x+dx]
    return [False, -1, -1]

def checkCurrentNumber(numberGearList, number, gears):
    if number != '':
        if(len(gears) > 0):
            numberGearList.append([int(number)] + gears)
        return numberGearList, '', []
    return numberGearList, number, gears


numberGearList = [] #[[number1,(gear1),(gear2),...], [number2,(gear3),(gear4),...]]

for y in range(len(schematic)):
    currentNumber = ''
    currentGears = []
    for x in range(len(schematic[0])):
        if schematic[y][x].isdigit():
            currentNumber += schematic[y][x]
            if isSymbolAdjacent(y, x)[0]:
                [b, y2, x2] = isSymbolAdjacent(y, x)
                if (y2, x2) not in currentGears:
                    currentGears.append((y2, x2))
        else:
            numberGearList, currentNumber, currentGears = checkCurrentNumber(numberGearList, currentNumber, currentGears)

    numberGearList, currentNumber, currentGears = checkCurrentNumber(numberGearList, currentNumber, currentGears)


#count how often a gear is linked to a number
gearCounts = defaultdict(int)
for n in numberGearList:
    for g in range(1, len(n)):
        currentGear = n[g]
        gearCounts[currentGear] += 1

#find gears 
validGears = [g for g, count in gearCounts.items() if count ==2]

#sum all products by finding the 2 numbers connected to every validGear
result = 0
for v in validGears:
    tempSum = 1
    for n in numberGearList:
        for i in range(1, len(n)):
            if n[i] == v:
                tempSum *= n[0]
    result += tempSum

print(result)
