def BinarySearch(nums, val):
    imin, imax = 0, len(nums)
    print('len is ', imax)
    i = (imin + imax) // 2
    while imin < imax:
        if nums[i] > val:
            imax = i - 1
        elif nums[i] < val:
            imin = i + 1
        else:
            return i
        i = (imin + imax) // 2
    return -i - 1


nums = [1, 3, 5, 7, 9, 12, 34]
val = 100
print(BinarySearch(nums, val))
