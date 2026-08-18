class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums=defaultdict(int)
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in dict_nums:
                return [dict_nums[comp], i]
            dict_nums[nums[i]]=i
        return False