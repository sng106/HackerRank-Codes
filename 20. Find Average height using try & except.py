'''
Sample Input:
4
76 64 55 33

Sample Output:
57.000

Finding average of 4 numbers
'''

try:
    # Read an integer n
    n = int(input())
    
    if n <= 0:
        print("Error: n must be a positive integer.")
    else:
        # Read n space-separated integers and convert them to a list of integers
        heights = list(map(int, input().split()))

        # Ensure that the number of heights matches n
        if len(heights) != n:
            print(f"Error: Expected {n} heights but got {len(heights)}")
        else:
            # Calculate the average of the heights
            average_height = sum(heights) / n
            
            # Print the average height formatted to 3 decimal places
            print(f"{average_height:.3f}")
except ValueError:
    print("Error: Invalid input. Please enter integers only.")
