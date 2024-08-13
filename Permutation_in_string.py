class Solution:
    # My Solution
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1

        while right <= (len(s2) - 1):
            if sorted(s2[left:right+1]) == sorted(s1):
                return True
            else:
                left += 1
                right += 1
        
        return False

    # Faster solution
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False

        # create freq arrays
        s1Freq = [0] * 26
        s2Freq = [0] * 26

        # calculate s1 freqs
        for i in range(len(s1)):
            s1Freq[ord(s1[i])-ord('a')] += 1
            s2Freq[ord(s2[i])-ord('a')] += 1
        
        if (s1Freq == s2Freq):
                return True
        
        # sliding window and compare substring maps with s1 map
        for r in range(len(s1), len(s2)):
            s2Freq[ord(s2[r]) - ord('a')] += 1
            s2Freq[ord(s2[r-len(s1)]) - ord('a')] -= 1
            if (s1Freq == s2Freq):
                return True

        return False
