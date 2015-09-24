
"""Insertion sorting algorithm"""
def insertion_sort(list_to_sort):
    for i in range(1, len(list_to_sort)):
        j = i
        while j >0 and list_to_sort[j-1] > list_to_sort[j]:
            temp_value = list_to_sort[j]
            list_to_sort[j] = list_to_sort[j-1]
            list_to_sort[j-1] = temp_value
            j = j-1

"""Regular selection sort algorithm"""
def selection_sort(list_to_sort):
    this_index = 0
    for j in range(0, len(list_to_sort)):
        min_index = j
        for i in range(this_index+1, len(list_to_sort)):
            if list_to_sort[i] < list_to_sort[min_index]:
                min_index = i
        if(min_index != j):
            temp_value = list_to_sort[j]
            list_to_sort[j] = list_to_sort[min_index]
            list_to_sort[min_index] = temp_value
        this_index+=1

"""Inefficient regular bubble sort""" 
def bubble_sort(list_to_sort):

    sorted = False
    while not sorted:
        #true to start, set false if have to swap elements
        sorted = True
        for i in range(1, len(list_to_sort)):
            #if adjacent elements are out of order, swap them
            if list_to_sort[i-1] > list_to_sort[i]:
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i-1]
                list_to_sort[i-1] = temp
                sorted = False

def shell_sort(list_to_sort):
    pass

def merge_sort(list_to_sort):
    pass

def hear_sort(list_to_sort):
    pass