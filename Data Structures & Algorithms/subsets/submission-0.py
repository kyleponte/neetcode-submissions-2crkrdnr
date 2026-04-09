class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def findSubsets(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            findSubsets(i + 1)

            subset.pop()
            findSubsets(i + 1)
        
        findSubsets(0)
        return res