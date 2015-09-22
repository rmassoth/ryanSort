

def insertion_sort(list_to_sort):
    pass

"""Regular selection sort algorithm"""
def selection_sort(list_to_sort):
    my_temp_list = []

    for i in range(0, len(list_to_sort)):
        

    list_to_sort = my_temp_list

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