file1 = open('input.txt', 'r')
Lines = file1.readlines()

cols = len(Lines[0])-1
rows = len(Lines)
#print("cols:" + str(cols))
#print("rows" + str(rows))
schematic = [['0' for _ in range(cols)] for _ in range(rows)]
for row in range(len(Lines)):
    for col, c in enumerate(Lines[row][0:len(Lines[0])-1]):
        schematic[row][col] = c

def isSymbol(x):
    if not x.isdigit() and x != '.':
        return 1
    else:
        return 0
def validPosition(y, x):
    return 0 <= y < rows and 0 <= x < cols

def isSymbolAdjacent(y, x):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dx, dy in directions:
        if validPosition(y+dy, x+dx):
            if isSymbol(schematic[y+dy][x+dx]):
                return True
    return False


numbers = []
for y in range(len(schematic)):
    currentNumber = ''
    currentNumberFlag = False
    for x in range(len(schematic[0])):
        if schematic[y][x].isdigit():
            currentNumber += schematic[y][x]
            #print(currentNumber)
            if isSymbolAdjacent(y, x):
                currentNumberFlag = True
        elif currentNumber != '':
            if(currentNumberFlag):
                numbers.append(int(currentNumber))
            currentNumber = ''
            currentNumberFlag = False
    if currentNumber != '':
        if(currentNumberFlag):
            numbers.append(int(currentNumber))

#print(len(numbers))
digits = [0,0,0]
for n in numbers:
    if n < 10:
        digits[0] += 1
    elif n < 100:
        digits[1] += 1
    else:
        digits[2] += 1
#print(digits)
print(sum(numbers))    

