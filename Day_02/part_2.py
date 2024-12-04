
# Open File and read puzzle input
# with open('puzzle_input', 'r') as text:
#     puzzle_input = text.read().splitlines()

# count = 0
# # Check if increasing, decreasing in safe zone
# def check_if_safe(check_list, remove=True):
#     ascending = int(check_list[0]) < int(check_list[1])
#     for x in range(1, len(check_list)):
#         if int(check_list[x]) <= int(check_list[x-1]) and ascending:
#             if remove:
#                 if x == 2:
#                     first_check = check_list.copy()
#                     first_check.pop(0)
#                     if check_if_safe(first_check, remove=False):
#                         return True
#                 check_list.pop(x)
#                 return check_if_safe(check_list, remove=False)
#             return False
#         if int(check_list[x]) >= int(check_list[x-1]) and not ascending:
#             if remove:
#                 if x == 2:
#                     first_check = check_list.copy()
#                     first_check.pop(0)
#                     if check_if_safe(first_check, remove=False):
#                         return True
#                 check_list.pop(x)
#                 return check_if_safe(check_list, remove=False)
#             return False
#         if abs(int(check_list[x]) - int(check_list[x-1])) > 3:
#             if remove:
#                 if x == 2:
#                     first_check = check_list.copy()
#                     first_check.pop(0)
#                     if check_if_safe(first_check, remove=False):
#                         return True
#                 check_list.pop(x)
#                 return check_if_safe(check_list, remove=False)
#             return False
#     return True

# count = 0
# # Check if increasing, decreasing in safe zone
# def check_if_safe(check_list, remove=True):
#     ascending = int(check_list[0]) < int(check_list[1])
#     for x in range(1, len(check_list)):
#         if int(check_list[x]) <= int(check_list[x-1]) and ascending:
#             if remove:
#                 if x == 2:
#                     first_check = check_list.copy()
#                     first_check.pop(0)
#                     print('Rechecking...', first_check)
#                     if check_if_safe(first_check, remove=False):
#                         return True
#                 remove = False
#                 continue
#             return False
#         if int(check_list[x]) >= int(check_list[x-1]) and not ascending:
#             if remove:
#                 if x == 2:
#                     first_check = check_list.copy()
#                     first_check.pop(0)
#                     print('Rechecking...', first_check)
#                     if check_if_safe(first_check, remove=False):
#                         return True
#                 remove = False
#                 continue
#             return False
#         if abs(int(check_list[x]) - int(check_list[x-1])) > 3:
#             if remove:
#                 if x == 2:
#                     first_check = check_list.copy()
#                     first_check.pop(0)
#                     print('Rechecking...', first_check)
#                     if check_if_safe(first_check, remove=False):
#                         return True
#                 remove = False
#                 continue
#             return False
#     return True


# Place input data into list
# for x in puzzle_input:
#     check = check_if_safe(x.split())
#     if check:
#         count += 1
#     else:
#         print(x.split())
# print(count)




# Check if a sequence is safe
def is_safe(sequence):
    ascending = int(sequence[0]) < int(sequence[1])
    for i in range(1, len(sequence)):
        current = int(sequence[i])
        previous = int(sequence[i - 1])
        
        # Check ascending/descending order and difference limit
        if (ascending and current <= previous) or (not ascending and current >= previous):
            return False
        if abs(current - previous) > 3:
            return False
    return True


# Check if removing one element can make the sequence safe
def can_be_safe_with_removal(sequence):
    for i in range(len(sequence)):
        # Create a new sequence excluding one element
        modified_sequence = sequence[:i] + sequence[i + 1:]
        if is_safe(modified_sequence):
            return True
    return False


# Count safe sequences in the input
def count_safe_reports(puzzle_input):
    count = 0
    for line in puzzle_input:
        sequence = line.split()  # Split the line into a list of levels
        if is_safe(sequence) or can_be_safe_with_removal(sequence):
            count += 1
        else:
            print("Unsafe sequence:", sequence)
    return count


# Read input and process
with open('puzzle_input', 'r') as text:
    puzzle_input = text.read().splitlines()

safe_count = count_safe_reports(puzzle_input)
print("Number of safe reports:", safe_count)