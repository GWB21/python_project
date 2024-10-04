def min_heapify_subtree(arr, target_node_index):

    smallest_i = target_node_index
    left_i = 2 * target_node_index + 1
    right_i = 2 * target_node_index + 2

    if left_i < len(arr) and arr[left_i] < arr[smallest_i]:
        smallest_i = left_i

    if right_i < len(arr) and arr[right_i] < arr[smallest_i]:
        smallest_i = right_i

    if smallest_i != target_node_index:
        arr[target_node_index], arr[smallest_i] = arr[smallest_i], arr[target_node_index]
        min_heapify_subtree(arr, smallest_i)

def change_to_min_heap(arr):
    last_parent_node_index = len(arr) // 2 - 1

    for last_parent_node_index in range(last_parent_node_index, -1, -1):
        min_heapify_subtree(arr, last_parent_node_index)

    return arr

def min_heap_sort (arr):
    sorted_by_ascending_order_array = []
    min_heap = change_to_min_heap(arr.copy())

    while min_heap:
            min_heap[0], min_heap[-1] = min_heap[-1], min_heap[0]
            sorted_by_ascending_order_array.append(min_heap.pop(-1))
            min_heapify_subtree(min_heap, 0)

    return sorted_by_ascending_order_array


arr = [7, 6, 5, 4, 2, 1, 3]
print(f"""
before sort : {arr}
 after sort : {min_heap_sort(arr)}""")

