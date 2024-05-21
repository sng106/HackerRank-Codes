'''
The builtins we used always tell for common one word, here we seprated the input and makes builtin works with it

Sample Input
qA2

Sample Output
True
True
True
True
True
'''
if __name__ == '__main__':
    s = input()
    print(any(char.isalnum() for char in s))  
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))

any() This function is used to get at least one iteraion of a particular condition.

#eg:
if __name__ == '__main__':
    s = qA2
    print(any(char.isalpha() for char in s))

#here I need to prove input is fully alpha, but normaly i used "isalpha" means it gives false so I am using any, so that in input there is one alphabet so it comes true
