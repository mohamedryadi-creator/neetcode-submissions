class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longueur = 0
        caracteres = set()

        for right in range(len(s)):
            while s[right] in caracteres:
                caracteres.remove(s[left])
                left += 1

            caracteres.add(s[right])
            longueur = max(longueur, right - left + 1)

        return longueur