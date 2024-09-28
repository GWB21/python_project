def max_heapify(arr, n, i):
    largest = i  # 부모 노드의 인덱스
    left = 2 * i + 1  # 왼쪽 자식 노드의 인덱스
    right = 2 * i + 2  # 오른쪽 자식 노드의 인덱스

    # 왼쪽 자식이 존재하고, 부모보다 큰 경우
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 존재하고, 가장 큰 노드보다 큰 경우
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 부모 노드가 자식보다 작은 경우, 값을 교환하고 재귀적으로 호출
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        max_heapify(arr, n, largest)

# 주어진 배열을 max-heap으로 변환하는 함수
def build_max_heap(arr):
    n = len(arr)

    # 마지막 부모 노드부터 시작해서 힙 속성을 재정립
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

# 예시 배열
arr = [1, 2, 3, 4, 5, 6, 7]
print("변환 전 배열:", arr)

# max-heapify 적용
build_max_heap(arr)
print("max-heapify 이후 배열:", arr)
