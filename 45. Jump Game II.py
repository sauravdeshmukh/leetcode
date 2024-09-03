class Solution:
    def jump(self, nums: List[int]) -> int:
        #### thoughts
        # create a list with last entry as 0
        # go in reverse and at each index,check all indices where we can jump, if -1, skip, else take 1+min(all the values) and assign to list at the index
        # return list[0]
        # O(n*m), O(n)
        #### OR from neetcode - 
        # bfs with 2 pointers l,r both starting at 0 showing current level of bfs
        # jumps = 0
        # for r till last index, 
        # find farthest index - max of farthest index and val + index for vals bw l and r
        # set l = r + 1 and r = farthest index, jumps += 1
        # return jumps
        # O(n), O(1)
        ### edge cases
        # if len nums 1, return 0
        
        if len(nums) == 1:
            return 0
        
        jumps = farthest = l = r = 0
        while r < len(nums) - 1:
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = 1 + r
            r = farthest
            jumps += 1
        return jumps
