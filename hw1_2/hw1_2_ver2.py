import random

#### At first, I implemented it recursively. But I realized that the recursion technique can have a maximum recursion depth error issue. (Although it's unlikely to happen in "simple tasks")
#### So I also implemented it iteratively. => Process of understanding the logic was quite difficult, but it was still quite interesting.

def merge_sort_3way_iterative(arr):
    size = 1
    while size < len(arr):
        for start in range(0, len(arr), size * 3):
            left_arr = arr[start:start + size]
            middle_arr = arr[start + size : start + (size * 2)]
            right_arr = arr[start + (size * 2) : start + (size * 3)]
            arr[start : start + (size * 3)] = merge_3way(left_arr, middle_arr, right_arr)
        size *= 3
    return arr

def merge_sort_3way_recursive(arr):
    if len(arr) <= 1:
        return arr

    # slice an array in three pieces
    third_length = len(arr) // 3 + 1   # why not len(arr) // 3 ? => This code informed me that it could potentially cause a recursion error. I overlooked the fact that in slicing, the right column index is exclusive.
    left = arr[:third_length]
    middle = arr[third_length:2 * third_length]
    right = arr[2 * third_length:]

    # sorting the arrays
    left = merge_sort_3way_recursive(left)
    middle = merge_sort_3way_recursive(middle)
    right = merge_sort_3way_recursive(right)

    return merge_3way(left, middle, right)

def merge_3way(arr1, arr2, arr3):
    i, j, k = 0, 0, 0                                                       # i = left array index, j = right array index, k = middle array index
    merged_arr = []

    while i < len(arr1) or j < len(arr2) or k < len(arr3):                  # Besides the two-way merge, "or" was the key.
        min_value = float('inf')                                            # finding the minimum value of three value

        if i < len(arr1):
            min_value = min(min_value, arr1[i])

        if j < len(arr2):
            min_value = min(min_value, arr2[j])

        if k < len(arr3):
            min_value = min(min_value, arr3[k])

        if i < len(arr1) and arr1[i] == min_value:                          # if index is lower than the length of array & if that is a min_value
            merged_arr.append(arr1[i])                                      # append it
            i += 1
        elif j < len(arr2) and arr2[j] == min_value:
            merged_arr.append(arr2[j])
            j += 1
        else:
            merged_arr.append(arr3[k])
            k += 1

    return merged_arr


arr = [random.randint(0, 100) for _ in range(20)]
print(f"""
target random generated array : {arr}
3 way merge iterative version : {merge_sort_3way_iterative(arr)}
3 way merge recursive version : {merge_sort_3way_recursive(arr)}""")