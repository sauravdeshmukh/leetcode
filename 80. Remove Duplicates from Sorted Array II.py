class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #### thoughts
        # 2 pointers, unique collector, unique finder
        # set unique value as 1st value of nums
        # unqiue finder runs till the end of nums and checks if it finds a uniqe value
        # unique collector takes value of unique finder and moves forward 1 step
        # O(n), O(1)
        # OR 
        # both starts at 2, unqiue finder runs till the end of nums and checks if it finds a uniqe value by checking if dff from unqiue finder - 2
        # edge cases
        # if len nums is 0,1,2 return 0,1,2
        
        if len(nums) <= 2:
            return len(nums)
        j = 2
        for i in range(2, len(nums)):
            if nums[j-2] != nums[i]:#did not understand
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
