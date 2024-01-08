from typing import List

# problem: https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            temp_word = ''.join(sorted(word))

            if temp_word in res:
                res[temp_word].append(word)
            else:
                res[temp_word] = [word]

        return list(res.values())
    

# TEST
strs = ["eat","tea","tan","ate","nat","bat"]

solution = Solution()
solution.groupAnagrams(strs)