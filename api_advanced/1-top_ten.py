#!/usr/bin/python3
"""
This module defines a function to retrieve and print the top 10 hot posts
of a specified subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid or an error occurs, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ALX-RedditProject/1.0'}
    params = {'limit': 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )

        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {})
        children = data.get("children", [])

        if not children:
            print(None)
            return

        for post in children:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)

