#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ALX-RedditProject/1.0'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check if request is successful and subreddit exists
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {})
        children = data.get("children", [])

        if not children:
            print(None)
            return

        for post in children:
            title = post.get("data", {}).get("title")
            if title:
                print(title)

    except Exception:
        print(None)

