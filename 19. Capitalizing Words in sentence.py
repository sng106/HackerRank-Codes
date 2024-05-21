'''
Sample Input:
hiii hello

Sample Output:
Hiii Hello

Just Capitalizing the Words in a sentance
'''
#Code:
def solve(s):
    return s.title()

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
