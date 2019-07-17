from collections import deque
from math import pi

queue = deque(['ankit', 'bharti', 'garima'])
print(queue)

queue.appendleft('kailash')
print(queue)

removed_name = queue.popleft()
print(removed_name)
print(queue)

values = [str(round(pi, i)) for i in range(6)]
print(values)