from unittest.mock import right

merged_arr = []
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else if len(arr):
        left_arr = arr[:len(arr)//2]
        right_arr = [x for x in arr if x not in left_arr]


print(merge_sort(arr))