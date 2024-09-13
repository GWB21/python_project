import random


def generate_arrays():
    # 1부터 10까지의 수를 랜덤하게 두 배열에 배치
    numbers = list(range(1, 11))
    random.shuffle(numbers)

    array1 = sorted(numbers[:5])
    array2 = sorted(numbers[5:])

    return array1, array2


def merge_sorted_arrays(arr1, arr2):
    # 병합 정렬을 사용하여 두 정렬된 배열을 병합
    merged_array = []
    i, j = 0, 0

    # 두 배열 모두 요소가 남아 있을 때까지 비교 및 병합
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # 하나의 배열의 모든 요소가 소진된 후, 나머지 배열의 요소를 추가
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array


def main():
    array1, array2 = generate_arrays()
    print(f"Array 1: {array1}")
    print(f"Array 2: {array2}")

    merged_array = merge_sorted_arrays(array1, array2)
    print(f"Merged Array: {merged_array}")


if __name__ == "__main__":
    main()
