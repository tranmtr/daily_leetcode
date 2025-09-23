class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split('.')
        arr2 = version2.split('.')
        len1 = len(arr1)
        len2 = len(arr2)
        i = 0
        while (i < len1 and i < len2):
            if (int(arr1[i]) > int(arr2[i])):
                return 1
            elif (int(arr1[i]) < int(arr2[i])):
                return -1
            i += 1
        while (i < len1):
            if (int(arr1[i]) > 0):
                return 1
            i += 1
        while (i < len2):
            if (int(arr2[i]) > 0):
                return -1
            i += 1
        return 0
version1 = "1.01"
version2 = "1.001"
S = Solution()
print(S.compareVersion(version1, version2))
