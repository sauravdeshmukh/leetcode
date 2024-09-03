class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #### thoughts
        # 2 pointers, instead of removing val, search for non_val and place in first k indices
        # pointers top_k and non_val_finder both starting from 0
        # for non_val_finder in nums, if finds, place in top_k, both + 1, else only non_val_finder +=1
        # return top_k
        # O(n), O(1)
        #### edge cases
        # if n == 0, return 0
        
        #edge case
        if len(nums) == 0:
            return 0

        top_k_pointer = non_val_finder = 0
        for non_val_finder in range(len(nums)):
            if nums[non_val_finder] != val:
                nums[top_k_pointer] = nums[non_val_finder]
                top_k_pointer += 1
        return top_k_pointer
