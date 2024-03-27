file1 = open('input.txt', 'r')
Lines = file1.readlines()

firstSearch = ["1", "2", "3", "4","5", "6", "7", "8", "9", "one","two", "three", "four", "five", "six", "seven", "eight", "nine"]
lastSearch = ["1", "2", "3", "4","5", "6", "7", "8", "9", "eno","owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]
sum = 0
for line in Lines:
    firstIndex = len(line)+ 1
    lastIndex = len(line) + 10
    for i in range(len(firstSearch)):
        result = line.find(firstSearch[i])
        if result != -1 and result < firstIndex:
            firstIndex = result
            first = i
    for i in range(len(lastSearch)):
        result = line[::-1].find(lastSearch[i])
        if result != -1 and result < lastIndex:
            lastIndex = result
            last = i
    if(first >= 9): first -= 8 
    else: first += 1
    if(last >= 9): last -= 8 
    else: last += 1
    sum += int(str(first) + str(last))
print(sum) 