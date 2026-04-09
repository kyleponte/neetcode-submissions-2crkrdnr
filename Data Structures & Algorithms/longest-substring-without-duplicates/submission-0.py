class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, R = 0, 0
        charSet = set()
        maxLen = 0

        while R < len(s):
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1
            charSet.add(s[R])
            R += 1
            maxLen = max(maxLen, len(charSet))
        
        return maxLen
        
