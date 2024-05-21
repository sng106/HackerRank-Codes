'''Sample Input 0
HackerRank.com presents "Pythonist 2".

Sample Output 0
hACKERrANK.COM PRESENTS "pYTHONIST 2".
'''
Code:
def swap_case(s):
    string=""
    for i in s:
        if i == i.upper():
            i=i.lower()
            string+=i
        elif i == i.lower():
            i = i.upper()
            string+=i
        else:
            string+=i
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
