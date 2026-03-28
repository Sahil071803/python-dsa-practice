
# nums = [3, 5, 6, 4, 8, 9, 10, 7, 1]
#
# n = len(nums)
# for i in range(1,n):
#     key = nums[i]
#     j = i-1
#
#     while j >= 0 and nums[j] > key:
#         nums[j+1] = nums[j]
#         j-= 1
#
#     nums[j+1] = key
#
# print(nums)

def insertionSort(self, arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

print insertioSort(arr)