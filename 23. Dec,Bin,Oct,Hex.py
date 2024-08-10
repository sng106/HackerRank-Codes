'''Input:
5

Output:
  1   1   1   1
  2   2   2  10
  3   3   3  11
  4   4   4 100
  5   5   5 101
'''
def print_formatted(number):
    width = len(bin(number)) - 2  # Determine the width needed for the binary representation
    
    for i in range(1, number + 1):
        # Print the numbers in different bases with appropriate formatting
        print(f"{i:>{width}} {oct(i)[2:]:>{width}} {hex(i)[2:].upper():>{width}} {bin(i)[2:]:>{width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
