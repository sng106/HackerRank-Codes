'''
Print the result of hash(t)

Sample Input 0

2
1 2
Sample Output 0

3713081631934410656
'''
n=int(input())
elements=map(int,input().split())
t=tuple(elements)
print(abs(hash(t)))
