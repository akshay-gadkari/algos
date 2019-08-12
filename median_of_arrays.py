# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

# Example 2:
nums1 = [3, 4, 100]
nums2 = [34, 45]
# The median is (2 + 3)/2 = 2.5

def median(nums1, nums2):
    ordered = []
    # combined = nums1 + nums2
    # lowest = combined[0]
    # i = 0
    # while len(combined) > 0:
    #     if combined[i] < lowest:
    #         lowest = combined[i]
    #     i += 1
    #     if i == len(combined):
    #         ordered.append(lowest)
    #         combined.remove(lowest)
    #         if combined:
    #             lowest = combined[0]
    #         i = 0
    i = 0
    j = 0
    # while i + j < (len(nums1) + len(nums2)):
    while i + j < (len(nums1) + len(nums2)):
        print(i, j)
        if i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                ordered.append(nums1[i])
                i += 1
            else:
                ordered.append(nums2[j])
                j += 1
        else:
            if i < len(nums1):
                ordered.append(nums1[i])
                i += 1
            if j < len(nums2):
                ordered.append(nums2[j])
                j += 1
    print(ordered)
median(nums1, nums2)
