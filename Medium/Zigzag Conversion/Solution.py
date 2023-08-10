# This seem like a recurring theme, I couldn't solve it and needed
# to find explanations online to get the answer.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if num of rows = 1 or bigger than length of s, can return string straight
        if numRows == 1 or numRows >= len(s):
            return s
        # creating empty char in list for the number of rows
        rows = ["" for row in range(numRows)]
        index = 0
        step = 1
        for char in s:
            # add the char to current index in list
            rows[index] += char
            # if index is 0 then step needs to increment by 1 and not go below.
            if index == 0:
                step = 1
            # if index is at the same as numRows, its time to reverse it.
            elif index == numRows - 1:
                step = -1
            # add step to index
            index += step
        return "".join(rows)