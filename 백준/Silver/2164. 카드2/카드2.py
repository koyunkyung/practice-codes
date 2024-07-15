import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
cards = deque([i for i in range(1,n+1)])

while len(cards)>1:
    cards.popleft()
    card = cards.popleft()
    cards.append(card)
print(cards[0])