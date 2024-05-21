'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

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

#or

N = int(input())
lst = []
args = []
switch = {
    "insert": lambda: lst.insert(int(args[0]), int(args[1])),
    "print": lambda: print(lst),
    "remove": lambda: lst.remove(int(args[0])),
    "append": lambda: lst.append(int(args[0])),
    "sort": lambda: lst.sort(),
    "pop": lambda: lst.pop(),
    "reverse": lambda: lst.reverse(),
}

for i in range(N):
    args = input().split()
    command = args.pop(0)
    switch.get(command)()

    
