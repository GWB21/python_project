import random
import sys

# 3-way 병합 정렬 함수
def merge_sort_3way_recursive(arr):
    if len(arr) <= 1:
        return arr

    third_length = len(arr) // 3 + 1
    left = arr[:third_length]
    middle = arr[third_length:2 * third_length]
    right = arr[2 * third_length:]

    # 각 부분을 재귀적으로 정렬
    left = merge_sort_3way_recursive(left)
    middle = merge_sort_3way_recursive(middle)
    right = merge_sort_3way_recursive(right)

    # 병합하여 결과 반환
    return merge_3way(left, middle, right)

# 세 부분 배열을 병합하는 함수
def merge_3way(left, middle, right):
    merged = []
    i = j = k = 0

    # 세 배열을 병합
    while i < len(left) or j < len(middle) or k < len(right):
        min_value = float('inf')

        if i < len(left):
            min_value = min(min_value, left[i])
        if j < len(middle):
            min_value = min(min_value, middle[j])
        if k < len(right):
            min_value = min(min_value, right[k])

        # 최소값을 병합된 배열에 추가하고, 해당 배열의 인덱스를 증가
        if i < len(left) and left[i] == min_value:
            merged.append(left[i])
            i += 1
        elif j < len(middle) and middle[j] == min_value:
            merged.append(middle[j])
            j += 1
        else:
            merged.append(right[k])
            k += 1

    return merged

# 예시 실행
arr = [random.randint(0, 100) for _ in range(20)]
print("정렬 전:", arr)
sorted_arr = merge_sort_3way_recursive(arr)
print("정렬 후:", sorted_arr)
