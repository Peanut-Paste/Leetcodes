class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dict with roman letter and the corresponding value
        total, d = 0, {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i, v in enumerate(s):
            # if previous letter is larger or equal then sum it
            if d[s[i - 1]] >= d[v] or i == 0:
                total += d[v]
            else:
                # else minus the multiplication of previous number to take away what we added too.
                total += d[v] - d[s[i - 1]] * 2
        return total