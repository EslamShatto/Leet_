#https://leetcode.com/problems/two-sum/solutions/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sol = []
        for n in range(len(nums)):
            holder = []
            holder = nums.copy()
            holder.remove(nums[n])
            if ((target - nums[n]) in (holder))  :
                sol.append(n)
        return sol
nums =[-3,4,3,90]
target =0
sol =[]
print(Solution.twoSum('',nums,target))
