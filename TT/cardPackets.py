import sys
from typing import List

def cardPackets(cards: List[int]) -> int:
    cards.sort()

    minimum = sys.maxsize
    for i in range(2, cards[len(cards) - 1] + 1):
        count = 0
        for card in cards:
            if 0 < (card % i):
                count += (i - card % i)
        #print(i, count)

        if minimum > count:
            minimum = count
    
    return minimum

if __name__ == '__main__':
    print(cardPackets([4, 7, 5, 11, 15]))
    print(cardPackets([0, 3, 4, 1, 5, 2]))
    print(cardPackets([3, 3, 3, 3]))