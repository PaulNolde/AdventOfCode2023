file1 = open('input.txt', 'r')
Lines = file1.readlines()

sum = 0
for line in Lines:
    first = 0
    last = 0
    for i, c in enumerate(line):
        if c.isdigit():
            first = c
            break
    for i, c in enumerate(line[::-1]):
        if c.isdigit():
            last = c
            break
    sum += int(first + last)

print(sum)      