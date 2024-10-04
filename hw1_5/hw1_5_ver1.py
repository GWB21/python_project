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
# .....The code is identical to Problem 3

def min_heapify_subtree(arr, target_node_index):

    smallest_i = target_node_index
    left_i = 2 * target_node_index + 1
    right_i = 2 * target_node_index + 2

    if left_i < len(arr) and arr[left_i] < arr[smallest_i]:                             # Only the signs have been changed from max_heapify
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

def find_median(arr):
    max_heap = max_heap_sort(arr.copy())
    min_heap = min_heap_sort(arr.copy())
    while max_heap:
        if min_heap[0] >= max_heap[0]:                                         # When the length is odd => it's the median value // when it's even => it's the value just past the middle
            return (min_heap[0] + max_heap[0]) / 2                             # so adding these and dividing by 2 gives the median
        if min_heap[0] != max_heap[0]:                                         # when it's not equal, then delete it
            del min_heap[0]
            del max_heap[0]

def add_num(arr, num):
    arr.append(num)
    print(f"median after add {num} : {find_median(arr)}")

arr = [1,2,3,4,5,6,7,8,9]
print(f"initail median : {find_median(arr)}")
add_list = [10, 11, 19, 15, 12]

for num in add_list:
    add_num(arr, num)

# find_median => 시간 복잡도 O(nlogn)인데, O(logn)으로도 만들수 있다고 해서 찾아봤는데, 잘 이해가 안되어서,, 그렇게 개발하지 못했습니다.
# 주석은 일부로 영어로 달았습니다. 영어랑 친해져야겠다고 생각해서.. ㅎㅎ