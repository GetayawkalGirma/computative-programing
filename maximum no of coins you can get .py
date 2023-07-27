
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)//3
        print(n)
        piles.sort()
        count = 0
        for i in range(n, len(piles), 2):
            count += piles[i]
        return count

        # piles.sort(reverse=True)
        # coins = 0
        # n = len(piles) // 3
        # for i in range(1, n*2, 2):
        #     coins += piles[i]
        # return coins




