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
    
    power = maxColor.get('red', 0) * maxColor.get('green', 0) * maxColor.get('blue', 0)
    gameSum += power

print(gameSum)
end_time = time.time()
execution_time = end_time - start_time


print(execution_time)