# part_2.py
# Day 4 - Part 2

import numpy as np

# Open File and read puzzle input
with open('puzzle_input', 'r') as text:
    puzzle_input = text.read().splitlines()

def check_xmas(a,b):
    if ((padded_array[a-1][b-1] == 'M' and padded_array[a+1][b+1] == 'S') or (padded_array[a-1][b-1] == 'S' and padded_array[a+1][b+1] == 'M')) and ((padded_array[a+1][b-1] == 'M' and padded_array[a-1][b+1] == 'S') or (padded_array[a+1][b-1] == 'S' and padded_array[a-1][b+1] == 'M')):
        return True  
    return False

# Convert to NumPy array
array = np.array([list(row) for row in puzzle_input])

# Add padding to the array
padded_array = np.pad(array, 1, mode='constant', constant_values=0)

# Locate all values of A
index_A = np.where(padded_array == 'A')

count = 0
for x in range(len(index_A[0])):
    if check_xmas(index_A[0][x], index_A[1][x]):
        count += 1

print(count)
