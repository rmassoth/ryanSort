import random
from ryanSort import sorters

#list used for sorting
my_list = []


for i in range(0, 1000):
    my_list.append(random.randrange(0, 999))

def sorted(list_to_check):
    for i in range(1, len(list_to_check)):
        if list_to_check[i-1] > list_to_check[i]:
            return False
    return True

def test_bubble_sort():
    sorters.bubble_sort(my_list)
    assert sorted(my_list)
