import sys
from collections import deque

queue = deque()
n = int(sys.stdin.readline())

for i in range(n):
    input = sys.stdin.readline().split()

    if input[0] == 'push':
        queue.append(int(input[1]))

    elif input[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()

    elif input[0] == 'size':
        print(len(queue))

    elif input[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif input[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif input[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])