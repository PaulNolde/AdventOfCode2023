from collections import defaultdict
import timeit

file1 = open('input.txt', 'r')
Lines = file1.readlines()

def setup():
    cards = defaultdict()
    for g in range(len(Lines)):
        parts = Lines[g].split('|')
        winning = list(map(int, parts[0].split()[2:]))
        myNumbers = list(map(int, parts[1].split()))
        hits = 0
        for n in myNumbers:
            if n in winning:
                hits+= 1
        #value = [card amount, hits per card]
        cards[g] = [1, hits]
    return cards

def part1(cards):
    return sum( 2**(card[1]-1) if card[1] > 0 else 0 for card in cards.values() )

def part2(cards):
    for g, w  in cards.items():
        for i in range(1,w[1]+1):
            if g+i < len(Lines):
                cards[g+i][0] += w[0]
    return sum(card[0] for card in cards.values())

def main():
    cards = setup()
    print(part1(cards))
    print(part2(cards))

main()

#just for timing
# execution_time = timeit.timeit(main, number=100)
# print(f"Average execution time: {execution_time / 100} seconds")