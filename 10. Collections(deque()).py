'''
Same as 9th one but here you can use appendleft, popleft like some new built in functions using impoting deque 
'''

from collections import deque
n=int(input())
b=deque()
for i in range(n):
    a=input().split()
    if a[0] == 'append':
        b.append(int(a[1]))
    if a[0] == 'appendleft':
        b.appendleft(int(a[1]))
    if a[0] == 'pop':
        b.pop()
    if a[0] == 'popleft':
        b.popleft()
print(" ".join(map(str, [i for i in b]))
