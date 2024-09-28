def three_way_merge_sort_iterative(arr):
    def three_way_merge(arr, start, mid1, mid2, end):
        left = arr[start:mid1]
        middle = arr[mid1:mid2]
        right = arr[mid2:end]

        i, j, k = 0, 0, 0
        m = start

        while i < len(left) and j < len(middle) and k < len(right):
            if left[i] <= middle[j] and left[i] <= right[k]:
                arr[m] = left[i]
                i += 1
            elif middle[j] <= left[i] and middle[j] <= right[k]:
                arr[m] = middle[j]
                j += 1
            else:
                arr[m] = right[k]
                k += 1
            m += 1

        while i < len(left):
            arr[m] = left[i]
            i += 1
            m += 1
        while j < len(middle):
            arr[m] = middle[j]
            j += 1
            m += 1
        while k < len(right):
            arr[m] = right[k]
            k += 1
            m += 1

    size = 1
    n = len(arr)

    while size < n:
        for start in range(0, n, size * 3):
            mid1 = start + size
            mid2 = start + size * 2
            end = min(start + size * 3, n)

            if mid1 < n and mid2 < n:
                three_way_merge(arr, start, mid1, mid2, end)
            elif mid1 < n:
                # 두 부분만 남은 경우 일반적인 2-way 병합 수행
                merge_two_way(arr, start, mid1, end)

        size *= 3

    return arr


def merge_two_way(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]

    i, j, k = 0, 0, start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


# 예시 실행
arr = [38, 27, 43, 3, 9, 82, 10, 15, 22, 56, 72, 61, 33, 21, 14, 46]
print("정렬 전:", arr)
three_way_merge_sort_iterative(arr)
print("정렬 후:", arr)
