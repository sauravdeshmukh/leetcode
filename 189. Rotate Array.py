class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #### thoughts
        # k = k % len nums
        # [1,2,3,4,5,6,7],3 input
        # [5,6,7,1,2,3,4] answer
        # [7,6,5,4,3,2,1] can reverse
        # [5,6,7,1,2,3,4] split by 0,k-1 and k to n-1 and reverse both parts
        # O(n), O(1)
        #### edge cases
        # if k == 0 (after k%len(nums)), return
        # if len nums is 1, return
        
        k = k % len(nums)
        if k == 0 or len(nums) == 1:
            return
        
        def rev(s: int, e: int) -> None:
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1
        
        rev(0, len(nums) - 1)
        rev(0, k - 1)
        rev(k, len(nums) -1)
