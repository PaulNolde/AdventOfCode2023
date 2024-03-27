import time

start_time = time.time()

file1 = open('input.txt', 'r')
Lines = file1.readlines()

gameSum = 0
contains = {'red': 12, 'green': 13, 'blue': 14}
for line in Lines:
    maxColor = {}
    cutGame = line.split(':')
    draws = cutGame[1].split(';')
    for d in draws:
        group = d.split(',')
        for g in group:
            parts = g.split()
            number = int(parts[0])
            color = parts[1]
            if maxColor.get(color, 0) < number:
                maxColor[color] = number
    
    if maxColor.get('red', 0) <= contains.get('red') and maxColor.get('green', 0) <= contains.get('green') and maxColor.get('blue', 0) <= contains.get('blue'):
        gameSum += int(cutGame[0].split()[1])

print(gameSum)
end_time = time.time()
execution_time = end_time - start_time


print(execution_time)

