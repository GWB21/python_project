import random
def merge_sort_3way_iterative(arr):
    size = 1
    while size < len(arr):
        for start in range(0, len(arr), size * 3):
            mid1 = start + size
            mid2 = start + size * 2
            end = min(start + size * 3, len(arr))

            # 세 부분 배열을 병합
            merge_3way(arr, start, mid1, mid2, end)

        # 다음 반복에서는 3배 크기의 부분 배열을 병합
        size *= 3
    return arr


def merge_3way(arr, start, mid1, mid2, end):
    # 세 부분 배열을 임시로 저장
    left = arr[start:mid1]
    middle = arr[mid1:mid2]
    right = arr[mid2:end]

    i, j, k, l = 0, 0, 0, start
    # 세 부분 배열을 비교하여 원래 배열에 병합
    while i < len(left) or j < len(middle) or k < len(right):
        # 각각의 배열에서 유효한 값을 비교하여 최소값을 선택
        min_value = float('inf')

        if i < len(left):
            min_value = min(min_value, left[i])
        if j < len(middle):
            min_value = min(min_value, middle[j])
        if k < len(right):
            min_value = min(min_value, right[k])

        # 최소값이 있는 배열의 값을 병합하고 인덱스 증가
        if i < len(left) and left[i] == min_value:
            arr[l] = left[i]
            i += 1
        elif j < len(middle) and middle[j] == min_value:
            arr[l] = middle[j]
            j += 1
        else:
            arr[l] = right[k]
            k += 1
        l += 1


# 예시 실행
arr = [random.randint(0, 100) for _ in range(20)]
print("정렬 전:", arr)
merge_sort_3way_iterative(arr)
print("정렬 후:", arr)
