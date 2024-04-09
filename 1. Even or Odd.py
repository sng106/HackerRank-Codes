'''
Given an integer, n, perform the following conditional actions:
Condition:
If n is odd, print WeirD
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Sample Input 0
3
Sample Output 0
Weird
.....................
Sample Input 1
24
Sample Output 1
Not Weird
'''
a=int(input())
if(a%2==1):
    print("Weird")
elif(a%2==0 and 2 <= a <= 5):
    print("Not Weird")
elif(a%2==0 and a>20):
    print("Not Weird")
elif(a%2==0 and 6 <= a <=20):
    print("Weird")
