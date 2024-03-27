import timeit

file1 = open('input.txt', 'r')
Lines = file1.readlines()


def setupLine(l):
    data = list(map(int, l.split()))
    return data

def part1():
    result = 0
    for line in Lines:
        data = []
        data.append(setupLine(line))
        notZero = True
        while notZero:
            newSeq = []
            notZero = False
            for i in range(len(data[-1])-1):
                diff = data[-1][i+1] -  data[-1][i]
                newSeq.append(diff)
                if diff != 0:
                    notZero = True
            data.append(newSeq)
        data[-1].append(0)
        for i in range(len(data)-1, 0, -1):
            data[i-1].append(data[i][-1] + data[i-1][-1])
        result += data[0][-1]
    print("Result Part 1: " +  str(result))

def part2():
    result = 0
    for line in Lines:
        data = []
        data.append(setupLine(line))
        notZero = True
        while notZero:
            newSeq = []
            notZero = False
            for i in range(len(data[-1])-1):
                diff = data[-1][i+1] -  data[-1][i]
                newSeq.append(diff)
                if diff != 0:
                    notZero = True
            data.append(newSeq)
        data[-1] = [0] + data[-1]
        for i in range(len(data)-1, 0, -1):
            data[i-1]  = [data[i-1][0] -  data[i][0]] + data[i-1]
        result += data[0][0]
    print("Result Part 2: " +  str(result))

# execution_time = timeit.timeit(part1, number=100)
# execution_time2 = timeit.timeit(part2, number=100)
# print(f"Average execution time Part1: {execution_time / 100} seconds")
# print(f"Average execution time Part2: {execution_time2 / 100} seconds")


part1()
part2()