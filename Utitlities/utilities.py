import math
import random


def swap(list_1, index_1, index_2):
    """
    :param list_1: This is a list
    :param index_1: This is the index to the first item
    :param index_2: This is the index to the second item
    :return: returns the list with index_1 and index_2 interchanged
    """
    temp = list_1[index_1]
    list_1[index_1] = list_1[index_2]
    list_1[index_2] = temp
    return list_1


# +----------------------------------------------------------------------------------------------+
# |                         BEGINNING OF INSERTION_SORT                                                      |
# +----------------------------------------------------------------------------------------------+
def insertion_sort(liste):
    """
    param liste: A list of items
    ;about: uses the insertion sort algorithm to sort a list of integers
    :returns: The list given in sorted order
    """
    list_length = len(liste)
    for index in range(1, list_length):
        key = liste[index]             # holds the element to be inserted
        counter_index = index - 1      # holds the current position for insertion
        while counter_index >= 0 and liste[counter_index] >= key:
            liste[counter_index + 1] = liste[counter_index]
            counter_index = counter_index - 1
        liste[counter_index + 1] = key
    return liste
# +---------------------------------------------------------------------------------------------+
# |                END OF INSERTION_SORT                                                        |
# +---------------------------------------------------------------------------------------------+


# +----------------------------------------------------------------------------------------------+
# |                         BEGINNING OF MERGE_SORT                                              |
# +----------------------------------------------------------------------------------------------+
def merge(list0, begin, middle, end):
    boundary1 = (middle - begin) + 1    # (boundary) size for left
    boundary2 = end - middle           # (boundary) size for right
    left = []                          # initialize lists left and right
    right = []
    for i in range(0, boundary1):
        left.append(list0[begin + i])
    for j in range(boundary2):
        right.append(list0[middle + j + 1])
    counter_for_left = 0
    counter_for_right = 0
    index = begin
    while counter_for_right < boundary2 and counter_for_left < boundary1:
        if left[counter_for_left] <= right[counter_for_right]:
            list0[index] = left[counter_for_left]
            counter_for_left += 1
        else:
            list0[index] = right[counter_for_right]
            counter_for_right += 1
        index += 1                        # This way the index can be incremented
    while counter_for_left < boundary1:
        list0[index] = left[counter_for_left]
        index += 1
        counter_for_left += 1
    while counter_for_right < boundary2:
        list0[index] = right[counter_for_right]
        index += 1
        counter_for_right += 1


def merge_sort(liste, begin, end):
    """
    :param; liste: A list of items.
    :param; begin: This specifies to the algorithm another boundary.
    :param; end: This is the boundary the algorithm uses in sorting the list.
    :returns: The given list in sorted order.
    """
    if begin < end:
        temp = begin + end
        middle = math.floor(temp/2)
        merge_sort(liste, begin, middle)
        merge_sort(liste, middle + 1, end)
        merge(liste, begin, middle, end)
    return liste
# +--------------------------------------------------------------------------------------------+
# |                END OF MERGE_SORT                                                           |
# +--------------------------------------------------------------------------------------------+


# +--------------------------------------------------------------------+
# |                 BEGINNING OF BINARY_SEARCH                         |
# +--------------------------------------------------------------------+
def binary_search(list0, begin, end, key):
    """

    :param; list0: A list of items
    :param; begin: A specification on the beginning of the list
    :param; end:  A specification on the end of the list
    :param; key: A item the algorithm searches for in the list
    :return: An index to the item if in the list or 0
    """
    if key > list0[end]:                           # Checks if the item is larger than the largest item in list
        print("Not in list too BIG")
        return 0
    if key < list0[begin]:                         # Checks is the item is smaller than the smallest item in list
        print("Not in list too SMALL")
        return 0
    middle = random.randrange(begin, end + 1)       # Selects a number at random in the given boundary
    if begin == end and key != list0[middle]:
        print("\nNot in list")
        return 0
    if middle < 0:
        print("\nNot in list")
        return 0
    if list0[middle] == key:
        print("\nItem is in index", middle)
        return middle
    if key < list0[middle]:
        binary_search(list0, begin, middle - 1, key)
    elif key > list0[middle]:
        binary_search(list0, middle + 1, end, key)

# +---------------------------------------------------------------+
# |            END OF BINARY_SEARCH                               |
# +---------------------------------------------------------------+


def x_sum(lis21, begin, next1, key, size):              # check how this can be modified to give only one result
    if size > begin and size >= next1:
        sums = lis21[begin] + lis21[next1]
        if sums == key:
            print("the sum is in index {0} and index {1}".format(begin, next1))
            return begin, next1
        else:
            x_sum(lis21, begin, next1 + 1, key, size)
            x_sum(lis21, begin + 1, next1, key, size)


def x_sum2(lists, key, end):
    for outer in range(0, end):
        for inner in range(outer + 1, end + 1):
            sumy = lists[outer] + lists[inner]
            if sumy == key:
                print("the sum is in index {0} and index {1}".format(outer, inner))
                # return inner, outer
    #  print("No indices can be summed to give ", key)

# +--------------------------------------------------------------+
# |             BEGINNING OF RANDOM_SEARCH                       |
# +--------------------------------------------------------------+


def random_search(list_2, key):
    for i in range(len(list_2)):
        holder = random.randrange(i, len(list_2))
        if list_2[holder] == key:
            return holder
        else:
            swap(list_2, holder, i)
    return 0
# +----------------------------------------------------------------+
# |                END OF RANDOM_SEARCH                            |
# +----------------------------------------------------------------+


# +--------------------------------------------------------------+
# |         BEGINNING OF HEAP_SORT                               |
# +--------------------------------------------------------------+
def parent(i):
    return math.floor(i/2) - 1


def left_part(i):
    if i == 0:
        return 1
    return_value = (2 * i) + 1
    return return_value


def right_part(i):
    if i == 0:
        return 2
    return_valued = (2 * i) + 2
    return return_valued


def h_max_heapify(list_01, index_01, heap):
    heap_size = heap
    lef = left_part(index_01)
    r = right_part(index_01)
    if lef <= heap_size and list_01[index_01] < list_01[lef]:
        largest = lef
    else:
        largest = index_01
    if r <= heap_size and list_01[largest] < list_01[r]:
        largest = r
    if largest != index_01:
        swap(list_01, index_01, largest)
        h_max_heapify(list_01, largest, heap)


def h_build_max_heap(list11):
    heap_size = len(list11) - 1
    var = math.floor(heap_size/2)
    for ind in range(var, -1, -1):
        h_max_heapify(list11, ind, heap_size)


def heap_sort(list_02):
    heap_size = len(list_02) - 1
    h_build_max_heap(list_02)
    for indic in range(len(list_02) - 1, 1, -1):
        swap(list_02, 0, indic)
        heap_size = heap_size - 1
        h_max_heapify(list_02, 0, heap_size)
# +----------------------------------------------------------------------------+
# |           END OF HEAP_SORT                                                 |
# +----------------------------------------------------------------------------+


def partition(list_12, begin_1, end_1):
    pivot_1 = list_12[end_1]
    counter_index = begin_1
    for i in range(begin_1, end_1):
        if list_12[i] <= pivot_1:
            swap(list_12, counter_index, i)
            counter_index += 1
    swap(list_12, counter_index, end_1)
    return counter_index


def randomized_partition(list_13, begin_2, end_2):
    pivot_2 = random.randrange(begin_2, end_2 + 1)
    swap(list_13, pivot_2, end_2)
    return partition(list_13, begin_2, end_2)


# +-------------------------------------------------------------------------------------------+
# |                  BEGINNING OF QUICKSORT                                                   |
# +-------------------------------------------------------------------------------------------+
def quicksort(list_14, begin_3, end_3):
    if begin_3 < end_3:
        half = randomized_partition(list_14, begin_3, end_3)
        quicksort(list_14, begin_3, half - 1)
        quicksort(list_14, half + 1, end_3)
    return list_14
# +------------------------------------------------------------------------------------------+
# |                 END OF QUICKSORT                                                         |
# +------------------------------------------------------------------------------------------+


# +------------------------------------------------------------------------------------------+
# |                 BEGINNING OF COUNTING SORT                                               |
# +------------------------------------------------------------------------------------------+
def counting_sort(list_13, element):
    new_list = []
    length = len(list_13)
    list_14 = list_13
    for integers_4 in range(element):
        new_list.append(0)
    for integer in range(length):
        new_list[list_13[integer]] = new_list[list_13[integer]] + 1
    for integers_2 in range(1, element):
        new_list[integers_2] = new_list[integers_2] + new_list[integers_2 - 1]
    for integers_3 in range(length, -1):
        list_14[new_list[list_13[integers_3]]] = list_13[integers_3]
        new_list[list_13[integers_3]] = new_list[list_13[integers_3]] - 1
    print(list_14)
# +-------------------------------------------------------------------------------------------+
# |             END OF COUNTING SORT                                                          |
# +-------------------------------------------------------------------------------------------+


if __name__ == "__main__":
    lis = list()
    lis2 = [12, 43, 4, 0, 89, 5, 90, 0, 77, 90, 67, 122, 1, 21, 994, 31, 484, 14]
    number = int(input("how many numbers: "))
    print("insertion sort")
    for integers in range(0, number):
        number_put = int(input("enter no:"))
        lis.append(number_put)
    print(lis)
    insertion_sort(lis)                     # insertion sort
    print(lis)
    print("merge sort")
    end1 = len(lis2) - 1
    print(lis2)
    merge_sort(lis2, 0, end1)               # merge sort
    print(lis2)
    binary_search(lis2, 0, end1, 89)        # binary search
    # print(x_sum(lis2, 0, 1, 123, end1))
    x_sum2(lis2, 95, end1)                 # the sum problem
    print(random_search(lis2, 994))        # random searching algorithm
    # print(lis2)
    # print(heap_sort(lis2))                 # the heap sort algorithm
    # print(lis2)
    counting_sort(lis2, 995)
    #  print(quicksort(lis2, 0, end1))
