"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        mapping = {}
        for i in range(n):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
                continue
            else:
                if t[i] in mapping.values():
                    return False
                mapping[s[i]] = t[i]
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isIsomorphic(s="egg", t="add"))
    print(solution.isIsomorphic(s="foo", t="bar"))
    print(solution.isIsomorphic(s="paper", t="title"))
