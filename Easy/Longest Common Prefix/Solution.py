class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result, boo, length = strs[0], True, len(strs[0])
        # Looping through the string of first element in list
        for i in strs[0]:
            # looping through the list
            for x in strs[1:]:
                # if result is not in the current element from starting to the length of result
                if result not in x[0:length]:
                    boo = False
                    # remove last letter from result
                    result = result[: length - 1]
                    # length of result - 1
                    length -= 1
            # if boo still true means result is in all element, break loop
            if boo == True:
                break
            boo = True
        return result
