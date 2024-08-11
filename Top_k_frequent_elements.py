class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        
        hmap = {}

        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]] = hmap.get(nums[i]) + 1
            else:
                hmap[nums[i]] = 1

        sorted_dict = dict(sorted(hmap.items(), key=lambda item: item[1], reverse=True))
        freq_list = list(sorted_dict.keys())[:k]

        return freq_list
