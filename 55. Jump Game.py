class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #### thoughts
        # create a hash table with 1 value set (last index: true)
        # from last index, go in reverse
        # if index + hash(value) for any value v in values is true enter in hash table index: true
        # O(n*max_value), O(n)
        # OR
        # set target as last index
        # for n in nums from reverse 2nd last index:
        # if index + n >= target, set target as index, else continue
        # return true if target is 0, else return false
        # O(n), O(1)
        ### edge cases
        # len nums 1, return true
        
        n = len(nums)
        if n == 1:
            return True
        
        target = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] + i >= target:
                target = i
        return True if target == 0 else False
                
