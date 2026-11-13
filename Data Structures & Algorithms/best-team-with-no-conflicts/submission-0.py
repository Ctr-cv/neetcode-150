class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores)) # (age, score)
        oldest = max(ages)
        ages.sort()
        # max sum till age i, highest score so far
        dp = [score for _, score in players]
        for i in range(len(players)):
            score = players[i][1]
            for j in range(i):
                prev_score = players[j][1]
                if prev_score <= score:
                    dp[i] = max(dp[i], dp[j] + score)
        return max(dp)
        

