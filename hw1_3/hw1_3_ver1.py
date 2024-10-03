def max_heapify_subtree(arr, target_node_index, array_length):
    array_length = len(arr)
    largest_i = target_node_index        # parent node of subtree
    left_i = 2 * target_node_index + 1   # left child node index
    right_i = 2 * target_node_index + 2  # right child node index

    if left_i < array_length and arr[left_i] > arr[largest_i]:                           # if left child exists & have a larger value than current largest node
        largest_i = left_i                                                               # assign the left as the largest node

    if right_i < array_length and arr[right_i] > arr[largest_i]:                         # The same applies to the right node
        largest_i = right_i

    if largest_i != target_node_index:                                                   # if the target node isn't the largest node, then swap it
        arr[target_node_index], arr[largest_i] = arr[largest_i], arr[target_node_index]  # swap
        max_heapify_subtree(arr, largest_i, array_length)                                # after swap, max-heapify the subtree of the swapped node

def change_to_max_heap(arr):
    array_length = len(arr)
    last_parent_node_index = array_length // 2 - 1

    for last_parent_node_index in range(last_parent_node_index, -1, -1):                 #Perform a bottom-up max-heapify process, starting from the last parent node to the root node.
        max_heapify_subtree(arr, last_parent_node_index, array_length)

    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
print(f"""
before max-heapify : {arr}
 after max-heapify : {change_to_max_heap(arr)}""")