from collections import deque

customQueue = deque(maxlen=3)
customQueue.append(1)
customQueue.append(2)
customQueue.append(1)
customQueue.append(4)
print(customQueue.clear())
print(customQueue)
