class Twitter:

    def __init__(self):
        self.users = defaultdict(list)
        self.following = defaultdict(set)
        self.post_count = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].append((self.post_count, tweetId))
        self.post_count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId]
        users_for_feed = users | {userId}

        posts = []
        for user in users_for_feed:
            user_posts = self.users[user]
            posts.extend(user_posts)

        heapq.heapify_max(posts)
        print(posts)
        res = []
        for _ in range(10):
            if posts:
                res.append(heapq.heappop_max(posts)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].discard(followeeId)
