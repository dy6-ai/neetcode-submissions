class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_strs=defaultdict(list)
        for word in strs:
            sorted_word="".join(sorted(word))
            grouped_strs[sorted_word].append(word)
        return list(grouped_strs.values())