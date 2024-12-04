import re

puzzle_input = []
# Open File and read puzzle input
with open('puzzle_input', 'r') as text:
    for line in text:
        puzzle_input.append(line)

my_list = []
for x in puzzle_input:
    my_list.append(re.findall(r'\d+',x))

def create_lists(my_list):
    list_1 = []
    list_2 = []
    for a in my_list:
        list_1.append(int(a[0]))
        list_2.append(int(a[1]))
    return list_1, list_2

def find_occurence():
    occurence = []
    for z in range(len(list_1)):
        occurence.append(list_1[z] * list_2.count(list_1[z]))
    return occurence

list_1, list_2 = create_lists(my_list)
occurence = find_occurence()
print(sum(occurence))