'''
Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''
n=int(input())
col=[]
for i in range(n):
    ref=[x.lower() for x in input().split()]
    label=ref[0]
    if label=='insert':
        col.insert(int(ref[1]),int(ref[2]))
    elif label=='append':
        col.append(int(ref[1]))
    elif label=='sort':
        col.sort()
    elif label=='remove':
        col.remove(int(ref[1]))
    elif label=='pop':
        col.pop()
    elif label=='reverse':
        col.reverse()
    elif label=='print':
        print(col)
    else:
        print("Error")
    
