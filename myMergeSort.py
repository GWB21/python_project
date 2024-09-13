import random
from random import randint

from mergeSort import merge_sorted_arrays

def insert_sort(arr):
    for i in range (1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def gen_two_ran_arr(arr_length, largest_num_in_arr):
    numbers = list(range(1, largest_num_in_arr))
    arr1 = []
    arr2 = []
    for _ in range (arr_length):
        element = numbers[randint(0, largest_num_in_arr - 1)]
        numbers.remove(element)
        arr1.append(element)
    for _ in range (arr_length):
        element = random.choice(numbers)
        numbers.remove(element)
        arr2.append(element)

    arr1 = insert_sort(arr1)
    arr2 = insert_sort(arr2)
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    merged_arr = []

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

# 하나의 배열의 모든 요소가 소진된 후, 나머지 배열의 요소를 추가
    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1


    print(f"Merged Array: {merged_arr}")


def main():
    gen_two_ran_arr(5, 100)



if __name__ == "__main__":
    main()