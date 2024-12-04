import re

puzzle_input = []
# Open File and read puzzle input
with open('puzzle_input', 'r') as text:
    for line in text:
        puzzle_input.append(line)

puzzle_string = ''.join(puzzle_input)

# Scan for mul(x,y)
data = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", puzzle_string)

# Multiply x*y
def mul(x,y):
    return x * y

results = []
do = True
for item in data:
    if item == "don't()":
        do = False
        continue
    if item == "do()":
        do = True
        continue
    if do:
        results.append(eval(item))

# Sum all
total_sum = sum(results)

print(total_sum)