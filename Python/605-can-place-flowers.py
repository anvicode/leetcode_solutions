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

    def canPlaceFlowers2(self, flowerbed: List[int], n: int) -> bool:
        fb = [0] + flowerbed + [0]
        for i in range(1, len(fb) - 1):
            if fb[i - 1] == 0 and fb[i] == 0 and fb[i + 1] == 0:
                n -= 1
                fb[i] = 1
        return n < 1
