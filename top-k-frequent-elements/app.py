from typing import List

# problem: https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        # sort list
        nums = sorted(nums)

        for n in nums:
            # increment counter
            if n in res:
                res[n] = res[n] + 1
            # else initiate count
            else:
                res[n] = 1

        # loop over dict values and send back the anything more than 1
        new_list = [key for key,value in res.items() if value >= k]
        return new_list        

nums = [1,1,1,2,2,3]
k = 2
solution = Solution()
solution.topKFrequent(nums, k)
