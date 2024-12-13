# part_1.py
# Day 7 - Part 1

import itertools

puzzle_input = []

# Open File and read puzzle input
with open('puzzle_input', 'r') as file:
    for line in file:
        # Remove any trailing whitespace
        line = line.strip()
        if line:  # Ensure the line is not empty
            # Split the line at ':' and process further
            key, values = line.split(":")
            key = int(key.strip())  # Convert the key to integer
            value_list = list(map(int, values.split()))  # Convert values to integers
            puzzle_input.append([key, value_list])

# Possible operations: add or multiply
operations = ["add", "multiply"]


# Function to evaluate a combination of operations
def evaluate_combination(values, ops):
    result = values[0]  # Start with the first value
    for i, op in enumerate(ops):
        if op == "add":
            result += values[i + 1]
        elif op == "multiply":
            result *= values[i + 1]
    return result

# Evaluate all combinations
results = []
for value in puzzle_input:
    # Generate all combinations of operations for len(values) - 1 slots
    all_combinations = itertools.product(operations, repeat=len(value[1]) - 1)
    for combination in all_combinations:
        result = evaluate_combination(value[1], combination)
        if result == value[0]:
            results.append(result)
            break

print(sum(results))

