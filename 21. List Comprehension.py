'''
Sample Input 0
1
1
1
2

Sample Output 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Example
x=1
y=1
z=1
n=2

Print an array of the elements that do not sum to n .
'''
a, b, c = [int(input()) for i in range(3)] #This logic is used to input giving enter and make another input to next line like ("\n")
n = int(input())
lst = [[i, j, k] for i in range(a + 1) for j in range(b + 1) for k in range(c + 1) if i + j + k != n]
print(lst)
