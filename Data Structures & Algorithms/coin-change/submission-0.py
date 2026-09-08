class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        ways = [float('inf')] * (amount + 1)  # index n represents number of coins to get to n

        # Iterate
        for i in range(amount + 1):
            for coin in coins:
                if coin > i: continue
                if ways[i - coin] != 0 or i == coin:
                    if i == coin:
                        ways[i] = 1
                    else:
                        ways[i] = min(1 + ways[i - coin], ways[i])
        if ways[amount] == float('inf'): return -1
        return ways[amount]
                

