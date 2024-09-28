import random

# def quick_sort(arr):                                       #sorting randomly generated 20 number of array
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[len(arr) // 2]
#         left = [x for x in arr if x < pivot]
#         middle = [x for x in arr if x == pivot]
#         right = [x for x in arr if x > pivot]
#         return quick_sort(left) + middle + quick_sort(right)

def three_way_merge_sort(arr):
    i = j = k = 0                                           # i = left array index, j = right array index, k = middle array index
    merged_arr = []
    left_arr = arr[:len(arr)//3]
    right_arr = arr[(len(arr)//3) * 2:]
    middle_arr = arr[len(arr)//3 : (len(arr)//3) * 2]

    while i < len(left_arr) or j < len(right_arr) or k < len(middle_arr):
        if i < len(left_arr) - 1:
            if left_arr[i] <= right_arr[j] and left_arr[i] <= middle_arr[k]:
                merged_arr.append(left_arr[i])
                i += 1
        if j < len(right_arr) - 1:
            if right_arr[j] <= left_arr[i] and right_arr[j] <= middle_arr[k]:
                merged_arr.append(right_arr[j])
                j += 1
        if k < len(middle_arr) - 1:
            if middle_arr[k] <= left_arr[i] and middle_arr[j] <= right_arr[j]:
                merged_arr.append(middle_arr[k])
                k += 1
    # merged_arr.extend(left_arr[i:])
    # merged_arr.extend(right_arr[j:])
    # merged_arr.extend(middle_arr[k:])

    return merged_arr

arr = [random.randint(0, 100) for _ in range(20)]
# print(quick_sort(arr))
# print(arr)
print(three_way_merge_sort(arr))