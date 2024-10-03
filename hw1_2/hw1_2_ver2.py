import random


def merge_sort_iterative(arr):
    # 병합할 부분 배열의 크기. 1부터 시작하여 2배씩 증가
    size = 1
    while size < len(arr):
        # 배열을 순회하면서 인접한 부분 배열들을 병합
        for start in range(0, len(arr), size * 2):
            mid = start + size
            end = min(start + size * 2, len(arr))
            # 두 부분 배열(start to mid, mid to end)을 병합
            merge(arr, start, mid, end)
        # 다음 반복에서는 두 배 크기의 부분 배열을 병합
        size *= 2
    return arr
dd

def merge(arr, start, mid, end):
    # 두 부분 배열을 임시로 저장
    left = arr[start:mid]
    right = arr[mid:end]

    i, j, k = 0, 0, start
    # 두 부분 배열의 원소를 비교하여 원래 배열에 정렬된 순서로 병합
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # 남은 원소들을 배열에 추가
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def three_way_merge_sort(arr):
    i = j = k = 0                                           # i = left array index, j = right array index, k = middle array index
    left_arr = merge_sort_iterative(arr[:len(arr)//3])
    right_arr = merge_sort_iterative(arr[(len(arr)//3) * 2:])
    middle_arr = merge_sort_iterative(arr[len(arr)//3 : (len(arr)//3) * 2])
    left_middle_arr =  merge_sort_iterative(left_arr + middle_arr)
    left_middle_right_merged_arr = merge_sort_iterative(left_middle_arr + right_arr)
    return left_middle_right_merged_arr

arr = [random.randint(0, 100) for _ in range(20)]
print(arr)
print(three_way_merge_sort(arr))
