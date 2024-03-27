import timeit

file1 = open('input.txt', 'r')
Lines = file1.readlines()

allHands = []
sortedHands = []

def resetLists():
    global allHands, sortedHands
    allHands,sortedHands = [], []
    
def mapCard(card, part):
    if part == 1:
        cardMap = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    else:
        cardMap = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}
    return cardMap[card]


def setupHands(part):
    global allHands
    for line in Lines:
        parts = line.split()
        hand = []
        cards = []
        for card in parts[0]:
            cards.append(mapCard(card,part))
        hand.append(cards)
        hand.append(int(parts[1]))
        allHands.append(hand)

def setTypesPart1():
    global allHands
    for hand in allHands:
        cardCounts = {i: 0 for i in range(2,15)}
        for card in hand[0]:
            cardCounts[card] += 1
        if 5 in cardCounts.values():
            hand.append(7)
        elif 4 in cardCounts.values():
            hand.append(6)
        elif 3 in cardCounts.values() and 2 in cardCounts.values():
            hand.append(5)
        elif 3 in cardCounts.values():
            hand.append(4)
        elif len([value for value in cardCounts.values() if value == 2]) == 2:
            hand.append(3)
        elif 2 in cardCounts.values():
            hand.append(2)
        else:
            hand.append(1)

def setTypesPart2():
    global allHands
    for hand in allHands:
        cardCounts = {i: 0 for i in range(1,15)}
        for card in hand[0]:
            cardCounts[card] += 1
        noJokers = {key: value for key, value in cardCounts.items() if key != 1}
        maxCount = cardCounts[max(noJokers, key=noJokers.get)]
        if maxCount == 5 or maxCount + cardCounts[1] >= 5:
            hand.append(7)
        elif maxCount == 4 or maxCount + cardCounts[1] >= 4:
            hand.append(6)
        elif fullHouse(cardCounts, noJokers):
            hand.append(5)
        elif maxCount == 3 or maxCount + cardCounts[1] >= 3:
            hand.append(4)
        elif twoPairs(cardCounts, noJokers):
            hand.append(3)
        elif 2 in cardCounts.values() or cardCounts[1] >= 1:
            hand.append(2)
        else:
            hand.append(1)

def fullHouse(cardCounts, noJokers):
    if 3 in cardCounts.values() and 2 in cardCounts.values():
        return True
    elif 3 in noJokers.values() and 1 in noJokers.values() and cardCounts[1] >= 1:
        return True
    elif len([value for value in noJokers.values() if value == 2]) == 2 and cardCounts[1] >= 1:
        return True
    elif 2 in noJokers.values() and cardCounts[1] >= 2:
        return True
    elif cardCounts[1] >= 3:
        return True
    
    return False

def twoPairs(cardCounts, noJokers):
    if len([value for value in cardCounts.values() if value == 2]) == 2:
        return True
    elif 2 in noJokers.values() and cardCounts[1] >= 1:
        return True
    elif cardCounts[1] >= 2:
        return True

def sortHands():
    global allHands, sortedHands
    sortedHands = sorted(allHands, key=lambda x: (x[2], x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]), reverse=True)

def score():
    result = 0
    for i in range(len(sortedHands)):
        result += sortedHands[i][1] * (len(sortedHands)-i)
    return result

def part1():
    resetLists()
    setupHands(1)
    setTypesPart1()
    sortHands()
    print(score())

def part2():
    resetLists()
    setupHands(2)
    setTypesPart2()
    sortHands()
    print(score())

def main():
    part1()
    part2()

main()

# execution_time = timeit.timeit(part1, number=100)
# execution_time2 = timeit.timeit(part2, number=100)
# print(f"Average execution time Part1: {execution_time / 100} seconds")
# print(f"Average execution time Part2: {execution_time2 / 100} seconds")