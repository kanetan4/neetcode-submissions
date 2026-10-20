import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.followmap = defaultdict(set) # followerId -> int: followeeIds -> Set[int]
        self.tweets = defaultdict(list) # userId -> int: tweetIds -> List[tuple(tweetcount, tweetId)]
        self.tweetcount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.tweetcount, tweetId])
        self.tweetcount -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        output = []
        h = [] # (count, tweetId, userId, index)

        # look through all users in the userId follow including himself, add the first of each to heap, den slowly add
        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                h.append((count, tweetId, followeeId, index - 1))
        heapq.heapify(h)

        while h and len(output) < 10:
            count, tweetId, followeeId, index = heapq.heappop(h)
            output.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(h, (count, tweetId, followeeId, index - 1))
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followmap:
            self.followmap[followerId] = set()
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
