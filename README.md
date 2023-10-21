# Django_Twitter_Server
Twitter Server with Django

## Endpoints

Below are the available API endpoints in the server:

```java
// User Endpoints
GET /api/users
GET /api/users/:username
POST /api/users
DELETE /api/users/:username
DELETE /api/users
PUT /api/users/:username

// Bio Endpoints
GET /api/bios
GET /api/users/:username/bio
POST /api/users/:username/bio
PUT /api/users/:username/bio
DELETE /api/users/:username/bio
DELETE /api/bios

// Follow Endpoints
POST /api/users/:username/follow
POST /api/users/:username/unfollow
GET /api/users/:username/followers
GET /api/users/:username/following
GET /api/follows

// Block Endpoints
POST /api/users/:username/block
POST /api/users/:username/unblock
GET /api/blocks
GET /api/users/:username/blockers
GET /api/users/:username/blocking

// Tweet Endpoints
POST /api/tweets
GET /api/tweets
GET /api/tweets/:tweetId
DELETE /api/tweets/:tweetId
DELETE /api/tweets
GET /api/users/:username/tweets
GET /api/timeline
POST /api/tweets/:tweetId/retweet
POST /api/tweets/:tweetId/quote
POST /api/tweets/:tweetId/reply
GET /api/tweets/:tweetId/replies
GET /api/tweets/:tweetId/retweets
GET /api/tweets/:tweetId/quotes

// Login Endpoint
POST /api/login

// Like Endpoints
GET /api/likes
GET /api/users/:username/likes
GET /api/tweets/:tweetId/likes
POST /api/tweets/:tweetId/like
POST /api/tweets/:tweetId/unlike

// Media Endpoints
GET /api/users/:username/profile-image
GET /api/users/:username/header-image
POST /api/users/:username/profile-image
POST /api/users/:username/header-image
GET /api/tweets/:tweetId/tweet-image
POST /api/tweets/:tweetId/tweet-image
```
