'''Sample Input
this is a string 

Sample Output
this-is-a-string
'''

Code:
def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
