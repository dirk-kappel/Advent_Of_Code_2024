puzzle_input = []
# Open File and read puzzle input
with open('puzzle_input', 'r') as text:
    for line in text:
        puzzle_input.append(line)

count = 0
# Check if increasing, decreasing in safe zone
def check_if_safe(check_list):
    ascending = int(check_list[0]) < int(check_list[1])
    for x in range(1, len(check_list)):
        if abs(int(check_list[x]) - int(check_list[x-1])) > 3:
            return False
        if int(check_list[x]) <= int(check_list[x-1]) and ascending:
            return False
        if int(check_list[x]) >= int(check_list[x-1]) and not ascending:
            return False
    return True


# Place input data into list
for x in puzzle_input:
    check = check_if_safe(x.split())
    if check:
        count += 1
print(count)




