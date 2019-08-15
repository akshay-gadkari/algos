arr = [4, 5, 6, 1, 2, 3]
target = 2
def shiftedBinarySearch(arr, target):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] == target:
            print(i)
            return i
        # if arr[i] < arr[i-1]:
            # print(i, arr[i])
            # new_arr = arr[i:]
            # new_arr += arr[:i]
            
    # half = len(new_arr) // 2
    # first_half = new_arr[:half]
    # second_half = new_arr[half:]
    # print(first_half)
    # print(second_half)
    # if target <= first_half[-1]:
    #     for i in range(len(first_half)):
    #         if first_half[i] == target:
    #             print(first_half[i])
    #             return (len(first_half) + second_half[i])
    # else:
    #     for i in range(len(second_half)):
    #         if second_half[i] == target:
    #             print(len(first_half) + second_half[i])
    #             return (len(first_half) + second_half[i])
shiftedBinarySearch(arr, target)
