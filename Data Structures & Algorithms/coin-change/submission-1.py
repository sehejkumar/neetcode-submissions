class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        my thinking is we can only go up to the amount and we can have
        elements in the array (indexes) correspond to amount
        '''

        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for currAmt in range(1, amount+1):
            for currCoin in coins:
                if currAmt - currCoin >= 0:
                    dp[currAmt] = min(dp[currAmt], 1 + dp[currAmt - currCoin])
            
        return dp[amount] if dp[amount] != float('inf') else -1

