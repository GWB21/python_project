import random

def merge_sort(arr):
    if len(arr) <= 1:                                      #doesn't need to be sorted when array has only one element or less.
        return arr
    else:                                                  # need to sort array because it's unsorted
        left_arr = arr[:len(arr) // 2]                     # slicing in two "nearly" equal length array -> it's not always equal because array length can be "odd"
        right_arr = arr[len(arr) // 2:]
        sorted_left_arr = merge_sort(left_arr)             # "Sorted" means ascending ordered , I used a recursion.
        sorted_right_arr = merge_sort(right_arr)           # after this left array and right array are sorted in ascending order
        return merge(sorted_left_arr, sorted_right_arr)

# merging two "ascending ordered" array function
def merge(left_arr, right_arr):
    i, j = 0, 0                                            # i => left_arr index    j => right_arr index // p.s didn't named like left_arr_index because looks complicated
    merged_arr = []                                        # declare merged array

    while i < len(left_arr) and j < len(right_arr):        # Do it until the merging of one array is complete // when one is complete then complete by just extending remaining array because it's sorted
        if left_arr[i] < right_arr[j]:                     # add the small one
            merged_arr.append(left_arr[i])
            i += 1
        else:
            merged_arr.append(right_arr[j])
            j += 1
        print(f"auxiliary space = {len(merged_arr)}\nmerged array = {merged_arr}")

    while i < len(left_arr):                               # just extending remaining sorted array
        merged_arr.append(left_arr[i])
        print(f"auxiliary space = {len(merged_arr)}\nmerged array = {merged_arr}")
        i += 1

    while j < len(right_arr):
        merged_arr.append(right_arr[j])
        print(f"auxiliary space = {len(merged_arr)}\nmerged array = {merged_arr}")
        j += 1

    return merged_arr

arr = [random.randint(0, 100) for _ in range(10)]
print(merge_sort(arr))