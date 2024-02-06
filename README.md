# ✨ Django_Twitter_Server

A Django project developed for learning purposes.

<br>

# 🚀 Getting Started

_These instructions will help you set up the project on your local machine._

## 🔧 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/MahdiHaeri/Django_Twitter_Server.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Django_Twitter_Server
    ```

3. (Optional) Set up and activate virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # for Linux/Mac
    .venv\Scripts\activate  # for Windows
    ```

4. Install dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

5. Create and apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Create an admin user:
    ```bash
    python manage.py createsuperuser
    ```

<br>

# 🧮 Start the Development Server

```bash
python manage.py runserver
```
_Open your web browser and visit “/admin/” on your local domain (e.g., http://127.0.0.1:8000/admin/) to access the admin interface._

<br>

# 🔗 Endpoints

- Admin: `/admin/`
- Users:
  - List all users: `/api/v1/users/`
  - Retrieve a user: `/api/v1/users/<int:user_id>/`
- Follows:
  - List all follows: `/api/v1/follows/`
  - Retrieve a follow: `/api/v1/follows/<int:follow_id>/`
- Blocks:
  - List all blocks: `/api/v1/blocks/`
  - Retrieve a block: `/api/v1/blocks/<int:block_id>/`
- Tweets:
  - List all tweets: `/api/v1/tweets/`
  - Retrieve a tweet: `/api/v1/tweets/<int:tweet_id>/`
- Retweets:
  - List all retweets: `/api/v1/retweets/`
  - Retrieve a retweet: `/api/v1/retweets/<int:tweet_id>/`
- Reply Tweets:
  - List all reply tweets: `/api/v1/reply_tweets/`
  - Retrieve a reply tweet: `/api/v1/reply_tweets/<int:tweet_id>/`
- Quote Tweets:
  - List all quote tweets: `/api/v1/quote_tweets/`
  - Retrieve a quote tweet: `/api/v1/quote_tweets/<int:tweet_id>/`
- Likes:
  - List all likes: `/api/v1/likes/`
  - Retrieve likes for a tweet: `/api/v1/likes/<int:tweet_id>/`
- Profiles:
  - List all profiles: `/api/v1/profiles/`
- JWT Token:
  - Obtain token: `/api/v1/token/` (POST)
  - Refresh token: `/api/v1/token/refresh/` (POST)
  - Verify token: `/api/v1/token/verify/` (POST)
