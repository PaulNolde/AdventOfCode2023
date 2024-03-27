import math
import timeit
file1 = open('input.txt', 'r')
Lines = file1.readlines()

time = list(map(int, Lines[0].split(':')[1].split()))
distance = list(map(int, Lines[1].split(':')[1].split()))

#part1
races = list(zip( time, distance))
#part2
bigTime = int(''.join(map(str, time)))
bigDistance = int(''.join(map(str, distance)))


#t = time
#r = record
#(t-x) * x = r
#-x^2 +tx = r
#-x^2 +tx - r = 0 
#x^2 -tx + r = 0

#-(t/2)+- sqrt((t/2)^2 - r)
def pqFormel(r):
    p = -r[0]
    q = r[1]
    x1 = math.floor(-p/2 - math.sqrt((p/2)**2 - q))
    x2 = math.ceil(-p/2 + math.sqrt((p/2)**2 - q))
    return x2-x1-1

def part1():
    result = 1
    for r in races:
        result *= pqFormel(r)
    return result

def part2():
    return pqFormel([bigTime, bigDistance])

def main():
    print(part1())
    print(part2())

main()
# execution_time = timeit.timeit(part1, number=100)
# print(f"Average execution time: {execution_time / 100} seconds")
# execution_time = timeit.timeit(part2, number=100)
# print(f"Average execution time: {execution_time / 100} seconds")