import random

def merge_sort_3way_iterative(arr):
    size = 1
    while size < len(arr):
        for start in range(0, len(arr), size * 3):
            left_arr = arr[start:start + size]
            middle_arr = arr[start + size : start + (size * 2)]
            right_arr = arr[start + (size * 2) : start + (size * 3)]
            # 세 부분 배열을 병합
            arr[start : start + (size * 3)] = merge_3way(left_arr, middle_arr, right_arr)

        # 다음 반복에서는 3배 크기의 부분 배열을 병합
        size *= 3
    return arr


def merge_3way(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    merged_arr = []
    # 세 부분 배열을 비교하여 원래 배열에 병합
    while i < len(arr1) or j < len(arr2) or k < len(arr3):
        # 각각의 배열에서 유효한 값을 비교하여 최소값을 선택
        min_value = float('inf')

        if i < len(arr1):
            min_value = min(min_value, arr1[i])
        if j < len(arr2):
            min_value = min(min_value, arr2[j])
        if k < len(arr3):
            min_value = min(min_value, arr3[k])

        # 최소값이 있는 배열의 값을 병합하고 인덱스 증가
        if i < len(arr1) and arr1[i] == min_value:
            merged_arr.append(arr1[i])
            i += 1
        elif j < len(arr2) and arr2[j] == min_value:
            merged_arr.append(arr2[j])
            j += 1
        else:
            merged_arr.append(arr3[k])
            k += 1

    return merged_arr


#예시 실행
arr = [random.randint(0, 100) for _ in range(20)]
print("정렬 전:", arr)
print("정렬 후:", merge_sort_3way_iterative(arr))

arr1 = [1, 3, 56, 98, 100]
arr2 = [11, 12, 34, 64, 88]
arr3 = [55, 57, 58, 60, 64]
print(merge_3way(arr1,arr2,arr3))