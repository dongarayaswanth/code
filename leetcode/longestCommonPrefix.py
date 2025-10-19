class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest = min(strs,key=len)
        for i,char in enumerate(shortest):
            for other_str in strs:
                if other_str[i] != shortest[i]:
                    return shortest[:i]
        return shortest

            

        