class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        unique = set(nums)
        for i in unique:
            if i-1 not in unique:
                current_num = i
                streak = 1
                while current_num + 1 in unique:
                    current_num += 1
                    streak += 1
                max_streak = max(streak, max_streak)

        return max_streak  
