# part_1.py
# Day 6 - Part 1

import numpy as np

# Open File and read puzzle input
with open('sample_input', 'r') as text:
    # puzzle_input = text.read().splitlines()
    puzzle_input = text.read().splitlines()

# Convert to NumPy array
array = np.array([list(row) for row in puzzle_input])

# Find starting point
start = np.where(array == '^')

# Find blockers
blockers = np.where(array == '#')
blockers = tuple(zip(*blockers))

# Find the starting coordinate
sc = int(str(start[0][0]) + str(start[1][0]))

# Add the coordinate to points traveled
points_traveled = set()
points_traveled.add(sc)

print(points_traveled)

# Initialize direction
direction = (0,1)
up = np.array([0,1])
print(up)
points_traveled.add(up)
def move(move_to_coordinate):
    if move_to_coordinate in my_blockers:
        return turn_90
    else:
        pass

# move()

# print((0,5) in my_blockers)