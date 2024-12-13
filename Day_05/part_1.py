# part_1.py
# Day 5 - Part 1

import math

# Open File and read puzzle input
with open('puzzle_input', 'r') as text:
    puzzle_input = text.read().splitlines()

def prepare_lists(my_list, split_value):
    temp_list = []
    for element in my_list:
        if split_value in element:
            split_items = element.split(split_value)
            temp_list.append(tuple(split_items))
    return temp_list

page_ordering_rules = prepare_lists(puzzle_input, '|')
page_number_updates = prepare_lists(puzzle_input, ',')

middle_page = []
def find_middle_page(my_list):
    for element in my_list:
        # Find the middle value of the page update
        middle_index = math.floor(len(element)/2)
        middle_page.append(int(element[middle_index]))

def create_key(page_ordering_rule):
    my_key = []
    for x in sorted(page_ordering_rule):
        if not my_key:
            my_key.append(x[0])
            my_key.append(x[1])
            continue
        if x[1] in my_key and x[0] not in my_key:
            # Insert element to the left of the found element
            my_key.insert(my_key.index(x[1]), x[0])
            continue
        # If the element is not yet in the key then insert and continue
        if x[1] not in my_key and x[0] not in my_key:
            my_key.append(x[0])
            my_key.append(x[1])
            continue
        # If the element on the right does not exist but the element on the left does then add it to the end
        if x[1] not in my_key and x[0] in my_key:
            my_key.append(x[1])
            continue
        # Check if the value is already to the left then continue
        if (x[1] in my_key and x[0] in my_key) and (my_key.index(x[0]) < my_key.index(x[1])):
            continue
        # If element is currently to the right of the value then move it to the left
        if (x[1] in my_key and x[0] in my_key) and (my_key.index(x[0]) > my_key.index(x[1])):
            my_key.remove(x[0])
            my_key.insert(my_key.index(x[1]), x[0])
            continue
    return my_key

good_updates = []
def check_updates(page_number_update, sorting_key):
    index_value = None
    for element in page_number_update:
        # print(element, '--->', sorting_key.index(element))
        if (index_value == None) or (sorting_key.index(element) > index_value):
            index_value = sorting_key.index(element)
            continue
        if sorting_key.index(element) < index_value:
            # print('Failed on', element)
            # print(sorting_key.index(element),'<', index_value)
            return
    good_updates.append(page_number_update)

def check_updates_1():
    for page_number_update in page_number_updates:
        apply_rules = []
        for page_ordering_rule in page_ordering_rules:
            if (page_ordering_rule[0] in page_number_update) and (page_ordering_rule[1] in page_number_update):
                apply_rules.append(page_ordering_rule)
        else:
            sorting_key = create_key(apply_rules)
        # print(page_number_update, sorting_key)
        check_updates(page_number_update, sorting_key)

check_updates_1()      

find_middle_page(good_updates)

print(sum(middle_page))
