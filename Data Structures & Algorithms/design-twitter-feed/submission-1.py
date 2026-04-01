class Twitter:

    def __init__(self):
        # Use a set for followees to avoid duplicates and allow O(1) removal
        self.followMap = {} # userId -> set(followeeIds)
        self.tweetMap = {}  # userId -> list of [count, tweetId]
        self.count = 0      # Global timestamp

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1 # Use negative numbers to turn min-heap into max-heap easily
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.tweetMap[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # Ensure the user is "following" themselves to see their own tweets
        if userId not in self.followMap:
            self.followMap[userId] = set()
        
        # We need to include the user themselves in the feed
        user_ids = self.followMap[userId] | {userId}

        for f_id in user_ids:
            if f_id in self.tweetMap:
                index = len(self.tweetMap[f_id]) - 1
                count, tweetId = self.tweetMap[f_id][index]
                # Push: (timestamp, tweetId, userId, index_of_next_tweet)
                heapq.heappush(minHeap, (count, tweetId, f_id, index - 1))

        while minHeap and len(res) < 10:
            count, tweetId, f_id, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                next_count, next_tweetId = self.tweetMap[f_id][idx]
                heapq.heappush(minHeap, (next_count, next_tweetId, f_id, idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        if followerId != followeeId: # Avoid following self (handled in getNewsFeed)
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)