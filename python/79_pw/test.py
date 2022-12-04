import collections as col

q = col.deque(range(10))

while q:
    print(q.popleft())
