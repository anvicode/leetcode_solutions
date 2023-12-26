class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_pointer, right_pointer = 0, 1
        current_earn = 0
        while right_pointer < len(prices):
            if prices[left_pointer] < prices[right_pointer]:
                potential_earn = prices[right_pointer] - prices[left_pointer]
                current_earn = max(potential_earn, current_earn)
            else:
                left_pointer = right_pointer
            right_pointer += 1
        return current_earn
