class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nl, total, length = [], 0, len(digits) - 1
        # if last digit is less then 9 then just plus one to it and return list
        if digits[length] < 9:
            digits[length] += 1
            return digits
        for i in digits:
            # convert the list into int
            total = total * 10 + i
        # plus one to the int
        total += 1
        # convert it back the new int to list
        for i in str(total):
            nl.append(int(i))
        return nl
