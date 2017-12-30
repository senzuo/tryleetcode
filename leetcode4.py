def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m, n = len(nums1), len(nums2)
    if m > n:
        n, m = m, n
        nums1, nums2 = nums2, nums1
    if m == 0:
        if n % 2 == 0:
            return (nums2[n // 2 - 1] + nums2[n // 2]) / 2
        else:
            return nums2[n // 2]
    # binary search
    imin, imax = 0, m

    while imax >= imin:
        i = (imin + imax) // 2
        j = (m + n + 1) // 2 - i
        if j > 0 and i < m and nums2[j - 1] > nums1[i]:
            imin = i + 1
        elif i > 0 and j < n and nums1[i - 1] > nums2[j]:
            imax = i - 1
        elif (i == 0 or j == n or nums1[i - 1] <= nums2[j]) and (j == 0 or i == m or nums2[j - 1] <= nums1[i]):
            # max_left
            if i == 0:
                max_left = nums2[j - 1]
            elif j == 0:
                max_left = nums1[i - 1]
            else:
                max_left = max(nums1[i - 1], nums2[j - 1])

            # min_right
            if i == m:
                min_right = nums2[j]
            elif j == n:
                min_right = nums1[i]
            else:
                min_right = min(nums1[i], nums2[j])

            if (m + n) % 2 == 0:
                return (max_left + min_right) / 2
            else:
                return max_left


nums1 = [4]
nums2 = [1, 2, 3]
print(findMedianSortedArrays(nums1, nums2))
