# part_1.py
# Day 4 - Part 1

import re
import numpy as np

# Open File and read puzzle input
with open('puzzle_input', 'r') as text:
    puzzle_input = text.read().splitlines()

# Convert to NumPy array
array = np.array([list(row) for row in puzzle_input])

def search_list(my_list):
    xmas_found = 0
    for element in my_list:
        xmas_found += len(re.findall(r"XMAS", element))
    return xmas_found

def search_list_backwards(my_list):
    xmas_found = 0
    for element in my_list:
        xmas_found += len(re.findall(r"SAMX", element))
    return xmas_found

def create_vertical_list():
    vertical_list = [''.join(col) for col in array.T]
    return vertical_list

# Function to extract all diagonals (major and minor)
def create_diagonal_list():
    diagonals = []
    
    # Major diagonals (top-left to bottom-right)
    for offset in range(-array.shape[0] + 1, array.shape[1]):
        diagonals.append(''.join(array.diagonal(offset)))
    
    # Minor diagonals (top-right to bottom-left)
    flipped_arr = np.fliplr(array)
    for offset in range(-flipped_arr.shape[0] + 1, flipped_arr.shape[1]):
        diagonals.append(''.join(flipped_arr.diagonal(offset)))
    
    return diagonals

vertical_list = create_vertical_list()
diagonal_list = create_diagonal_list()

# Define a dictionary to hold the results
search_results = {
    "horizontal": search_list(puzzle_input),
    "backwards": search_list_backwards(puzzle_input),
    "up_down": search_list(vertical_list),
    "down_up": search_list_backwards(vertical_list),
    "diagonals": search_list(diagonal_list),
    "diagonals_backwards": search_list_backwards(diagonal_list)
}

# Sum all values
total_occurrences = sum(search_results.values())
print(search_results)
# Output results
print(f"Total occurrences: {total_occurrences}")

