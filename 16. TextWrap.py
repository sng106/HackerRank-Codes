'''
Sample Input 0
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''
code:
import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    words = wrapper.fill(text=string)
    return words

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)

#or

import textwrap

def wrap(string, max_width):
    words = textwrap.wrap(string, max_width)
    return words

string, max_width = input(), int(input())
result = wrap(string, max_width)
for i in result:
    print(i)
