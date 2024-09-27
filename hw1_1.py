def merge_sort(arr1, arr2):
    i = 0
    j = 0
    merged_arr = []  #auxiliary space
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1
        print(f"merged array : {merged_arr}\nauxiliary space : {len(merged_arr)}\n")

    while i < len(arr1):
        merged_arr.append(arr1[i])
        print(f"merged array : {merged_arr}\nauxiliary space : {len(merged_arr)}\n")
        i += 1
    while j < len(arr2):
        merged_arr.append(arr2[j])
        print(f"merged array : {merged_arr}\nauxiliary space : {len(merged_arr)}\n")
        j += 1

arr1 = [1, 21, 38, 64, 95]
arr2 = [4, 20, 40, 55, 63]

merge_sort(arr1, arr2)

