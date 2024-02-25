class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus_one = int("".join([str(n) for n in digits])) + 1
        return [int(digit) for digit in str(plus_one)]

    def plusOne2(self, digits: List[int]) -> List[int]:
        i = 0
        one = 1
        digits = digits[::-1]
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(one)
                one = 0
            i += 1
        return digits[::-1]
