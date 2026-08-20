class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict=defaultdict(int)
        for i in range(len(nums)):
            nums_dict[nums[i]]+=1
        a=sorted(nums_dict,key=nums_dict.get, reverse=True)
        return a[:k] 
