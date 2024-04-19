import sys
from collections import deque

input = sys.stdin.readline

cards = deque()
for i in range(int(input())):
    cards.append(i + 1)

cards.reverse()

while len(cards) > 1:
    cards.pop()
    cards.appendleft(cards.pop())

print(cards.pop())
