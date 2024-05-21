'''
Sample Input
STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'

Sample Output
abrackdabra
Replacing word using position number
'''
#Code:
def mutate_string(string, position, character):
    if True:
        string=string[:position]+character+string[position+1:]
        return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
