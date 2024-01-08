from typing import List

# problem: https://leetcode.com/problems/top-k-frequent-elements/description/
# solution: using bucket sort
#          xref: https://www.youtube.com/watch?v=YPTqKIgVk-k

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # would result in {1: 3, 2: 2, 3:1, 4: 3 ....}

        for n, c in count.items():
            freq[c].append(n)
        # would result in [ 0[] 1[3] 2[2] 3[1,4] ]

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
     

nums = [1,1,1,2,2,3]
k = 1
solution = Solution()
solution.topKFrequent(nums, k)
