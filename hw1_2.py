def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def three_way_merge_sort(arr):
    i = j = k = 0
    merged_arr = []
    left = arr[:len(arr)//3]
    right = arr[(len(arr)//3) * 2:]
    middle = arr[len(arr)//3 : (len(arr)//3) * 2]

arr = [1,6,34,8,345,7,9,567,777, 999]
print(quick_sort(arr))
print(three_way_merge_sort(quick_sort(arr)))