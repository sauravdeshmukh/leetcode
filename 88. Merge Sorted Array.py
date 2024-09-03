class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ##### thoughts
        # copy nums2 to num1 from m index O(n)
        # sort - O(nlog(n))
        # overall - O(nlog(n)), O(1)
        ##### OR
        # copy list1 to a new list of size m
        # use 2 pointers to sort like above
        # O(n+m), O(m)
        ##### OR
        # does not work if copy nums1 elements to n in same list and find small elements to fill
        # O(n+m), O(1)
        ##### OR
        # instead of filling from 0 index, fill from last index
        # start from end of both lists and fill at m+n-1
        # find bigger elements
        # fill remaining from nums2, no need to fill remaining from nums1
        # O(n+m), O(1)
        ##### edge cases-
        # if n == 0, return list1
        # if m == 0, copy list2 to list1 and return list1
        
        if n == 0:
            return
        if m == 0:
            for i,v in enumerate(nums2):
                nums1[i] = v
            return

        p1 = m - 1
        p2 = n - 1
        a = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[a] = nums1[p1]
                p1 -= 1                
            else:
                nums1[a] = nums2[p2]
                p2 -= 1
            a -= 1
        
        while p2 >= 0:
            nums1[a] = nums2[p2]
            p2 -= 1
            a -= 1
