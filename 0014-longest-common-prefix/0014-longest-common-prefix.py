class Solution(object):
    def longestCommonPrefix(self, strs):

        prefix = strs[0]

        for word in strs[1:]:

            while word.find(prefix) != 0:

                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix


strs = ["dog", "racecar", "car"]

obj = Solution()

print(obj.longestCommonPrefix(strs))