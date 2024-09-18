a = [1, 17, 47, 67, 88]
b = [3 , 12, 36, 59, 66]
c = [ 3, 1234, 4, 1, 46]
def merge_sort(arr1, arr2):
    i = 0
    j = 0
    merged_arr =[]
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    # while i < len(arr1):
    #     merged_arr.append(arr1[i])
    #     i += 1
    #
    # while j < len(arr2):
    #     merged_arr.append(arr2[j])
    #     j += 1

    #정말 생각지도 못한 방식이군! extend메소드로 그냥 i번째부터 가져다가 붙여버린다니.. 너무 똑똑한걸
    merged_arr.extend(arr1[i:])
    merged_arr.extend(arr2[j:])

    return merged_arr

def insert_arr(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(merge_sort(a, b))
print(insert_arr(c))
