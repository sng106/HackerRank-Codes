'''
Sample Input :
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output :
56.00

Explain: malavika = 52+56+60/3==56.00
'''

n=int(input())
student_marks={}
for i in range(n):
    name, *line=input().split()
    scores=list(map(float, line))
    student_marks[name]=scores

query_name=input()
values=student_marks[query_name]
j=0
for i in values:
    j=i+j
k=j/len(values)
print("{:.2f}".format(k))
