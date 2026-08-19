class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = defaultdict(int)
        res=0
        max_count=0
        for i in range(len(nums)):
            nums_dict[nums[i]]+=1
            if max_count< nums_dict[nums[i]]:
                res=nums[i]
                max_count=nums_dict[nums[i]]
        return res