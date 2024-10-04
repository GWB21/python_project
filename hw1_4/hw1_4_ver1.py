import random
def max_heapify_subtree(arr, target_node_index):
    largest_i = target_node_index        # parent node of subtree
    left_i = 2 * target_node_index + 1   # left child node index
    right_i = 2 * target_node_index + 2  # right child node index

    if left_i < len(arr) and arr[left_i] > arr[largest_i]:                               # if left child exists & have a larger value than current largest node
        largest_i = left_i                                                               # assign the left as the largest node

    if right_i < len(arr) and arr[right_i] > arr[largest_i]:                             # The same applies to the right node
        largest_i = right_i

    if largest_i != target_node_index:                                                   # if the target node isn't the largest node, then swap it
        arr[target_node_index], arr[largest_i] = arr[largest_i], arr[target_node_index]  # swap
        max_heapify_subtree(arr, largest_i)                                              # after swap, max-heapify the subtree of the swapped node

def change_to_max_heap(arr):
    last_parent_node_index = len(arr) // 2 - 1

    for last_parent_node_index in range(last_parent_node_index, -1, -1):                 #Perform a bottom-up max-heapify process, starting from the last parent node to the root node.
        max_heapify_subtree(arr, last_parent_node_index)

    return arr

def max_heap_sort (arr):
    sorted_by_descending_order_array = []
    max_heap = change_to_max_heap(arr.copy())                                              # object reference (very interesting)

    while max_heap:                                                                        # do it until the length of array is 0 (big impressed by the "truthy" concept )
        max_heap[0], max_heap[-1] = max_heap[-1], max_heap[0]                              # swap the largest one and last leaf node
        sorted_by_descending_order_array.append(max_heap.pop(-1))                          # pop the last leaf node (that have the largest value among the entire array)
        max_heapify_subtree(max_heap, 0)                                   # after pop re-max-heapify

    return sorted_by_descending_order_array                                                # return the result

arr = [random.randint(0,100) for _ in range(20)]
arr_for_check = sorted(arr, reverse = True)

print(f"""
before sort         : {arr}
 after sort         : {max_heap_sort(arr)}
**** To check for correctness
sort func in python : {arr_for_check}""")