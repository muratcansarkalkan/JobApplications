# You will have an orthogonal triangle input from a file and you need to find the maximum sum of the numbers according to given rules below;

# 1. You will start from the top and move downwards to an adjacent number as in below.
# 2. You are only allowed to walk downwards and diagonally.
# 3. You can only walk over NON PRIME NUMBERS.
# 4. You have to reach at the end of the pyramid as much as possible.
# 5. You have to treat the input as pyramid.

import sympy

file = input("Specify the file you want to have a sum")

def linestonumbers(file):
    # read lines
    handle = open(file)
    lines = handle.readlines()
    # convert to array of strings
    pyramid_string = [l.split() for l in lines]
    # convert to numbers to perform operations
    pyramid_numbers = [[int(s) for s in p] for p in pyramid_string]
    return pyramid_numbers

def maximum_path_finding_sum(value, m):
    """
    Path finding algorithm
    """
    # Loop for bottom-up calculation
    for i in range(m-1, -1, -1):
        for j in range(i+1):
            # Checks if only the number is not prime as it was asked in challenge
            if sympy.isprime(j) == False:
            # For each element, check elements that are below directly or diagonally. Add the maximum of them to it
                if (value[i+1][j] > value[i+1][j+1]):
                    value[i][j] += value[i+1][j]
                else:
                    value[i][j] += value[i+1][j+1]
                # if (value[i+1][j] > value[i+1][j+1]) and (value[i+1][j] > value[i+1][j-1]):
                #     value[i][j] += value[i+1][j]
                # elif (value[i+1][j-1] > value[i+1][j+1]) and (value[i+1][j-1] > value[i+1][j]):
                #     value[i][j] += value[i+1][j-1]
                # else:
                #     value[i][j] += value[i+1][j+1]
    # Return the element which stores the maximum sum
    return value[0][0]


if __name__ == "__main__":
    value = linestonumbers(file)
    max_path_sum = maximum_path_finding_sum(value, len(value)-1)
    print(f'The optimal path sum is: {max_path_sum}')
