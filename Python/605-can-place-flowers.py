class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        for i in range(l):
            if (l == 1 and (flowerbed[0] == 1 or flowerbed[0] == 0) and n == 0) or (
                l == 1 and flowerbed[0] == n - 1
            ):
                return True
            if (l == 1 and flowerbed[0] == 1 and n != 0) or (
                l == 1 and flowerbed[0] != n - 1
            ):
                return False

            if i == 0 and (flowerbed[i] == 0 and flowerbed[i + 1] == 0):
                n -= 1
                flowerbed[i] = 1
            elif i == (l - 1) and (flowerbed[i] == 0 and flowerbed[i - 1] == 0):
                n -= 1
                flowerbed[i] = 1
            elif flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
        return n < 1
