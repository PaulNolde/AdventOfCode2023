from math import gcd
import timeit
file1 = open('input.txt', 'r')
Lines = file1.readlines()


def setup(part):
    setInstruct = True
    instruct = None
    waypoints = dict()
    start = []

    for line in Lines:
        if setInstruct:
            instruct = line
            setInstruct = False
        elif len(str(line))> 5:
            key, value = map(str.strip, line.split("="))
            value = value[1:-1].replace(" ", "")
            value = tuple(value.split(","))
            waypoints[key] = value
            if part == 2:
                if key[2] == 'A':
                    start.append(key)
    if part == 2:
        return instruct, waypoints, start
    return instruct, waypoints

def part1():
    instruct, waypoints = setup(1)
    currWaypoint = 'AAA'
    goalWaypoint = 'ZZZ'
    steps = 0
    while currWaypoint != goalWaypoint:
        direction = instruct[steps % (len(instruct)-1)]
        if direction == 'L':
            currWaypoint = waypoints[currWaypoint][0]
        else:
            currWaypoint = waypoints[currWaypoint][1]
        steps+= 1

    return steps



def checkEnd(p):

    if p[2] != 'Z':
        return False
    return True

def kgV(steps):
    kgV = 1
    for i in steps:
        kgV = kgV*i//gcd(kgV, i)
    return kgV

def part2():
    instruct, waypoints, start = setup(2)
    steps = 0
    stepList = []
    for s in start:
        currWaypoint = s
        steps = 0
        while not checkEnd(currWaypoint):
            direction = instruct[steps % (len(instruct)-1)]
            if direction == 'L':
                currWaypoint = waypoints[currWaypoint][0]
            else:
                currWaypoint = waypoints[currWaypoint][1]
            steps+= 1
        stepList.append(steps)
    return kgV(stepList)
    


# execution_time = timeit.timeit(part1, number=100)
# execution_time2 = timeit.timeit(part2, number=100)
# print(f"Average execution time Part1: {execution_time / 100} seconds")
# print(f"Average execution time Part2: {execution_time2 / 100} seconds")

print(part1())
print(part2())
