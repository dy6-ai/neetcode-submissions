class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_dict=defaultdict(int)
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in comp_dict:
                return [comp_dict[comp],i]
            comp_dict[nums[i]]=i
        