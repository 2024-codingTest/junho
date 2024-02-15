import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
cards = [i for i in range(1, n+1)]
cards = deque(cards)

while(len(cards)>1):
    cards.popleft()
    cards.append(cards[0])
    # cards.append(cards.popleft())
    cards.popleft()

print(cards[0])