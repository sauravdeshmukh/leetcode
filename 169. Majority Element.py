class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #### thoughts
        # run through nums and use hash map, to store count of occurrence of unique elements
        # run through hash map items, get key with value > len(nums)//2
        # O(n), O(n)
        # OR MOORE's VOTING ALGO
        # set count, candidate to 0
        # for n in nums, if count is 0, set candidate as n as count increase by 1, else if candidate is num, increase count by 1 else decrease count by 1
        # return candidate
        # O(n), O(1)
        # edge cases
        # if len nums 1, return 1st element
        if len(nums) == 1:
            return nums[0]
        count = candidate = 0
        for n in nums:
            if count == 0:
                candidate = n
                count += 1
            else:
                if candidate == n:
                    count += 1
                else:
                    count -= 1
            print(n,count, candidate)
        return candidate
            
