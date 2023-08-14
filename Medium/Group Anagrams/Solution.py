class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        # Create the keys first
        for s in strs:
            # Sorted makes it so that anagram strs will have the same output
            sorted_s = tuple(sorted(s))
            anagram[sorted_s] = []
        # Then map the values into those keys
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram[sorted_s].append(s)
        # Return the values only
        return anagram.values()