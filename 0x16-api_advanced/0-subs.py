#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyBot/1.0 (by /u/YourUsername)"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

# Example usage:
subreddit = "python"
print("Subscribers in r/python:", number_of_subscribers(subreddit))

subreddit = "invalid_subreddit"
print("Subscribers in invalid_subreddit:", number_of_subscribers(subreddit))
