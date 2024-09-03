class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #### thoughts
        # 2 pointers, unique_collector, unique_finder
        # unique_finder runs till the end of nums
        # unique_collector takes value of unique_finder and moves ahead when unique_finder finds a unique value (unique if diff from previous value as sorted list)
        # return unique_collector
        # O(n), O(1)
        # edge cases
        # if len nums == 0,1, return 0,1
        
        j, i  = 1, 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
