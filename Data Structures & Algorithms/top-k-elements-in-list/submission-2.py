class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict=defaultdict(int)
        for i in range(len(nums)):
            nums_dict[nums[i]]+=1
        def get_items(x):
            return nums_dict[x]
        a=sorted(nums_dict,key=get_items, reverse=True)
        return a[:k] 
