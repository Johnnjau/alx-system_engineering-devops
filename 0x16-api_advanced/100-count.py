#!/usr/bin/python3
import requests


def count_words(subreddit, word_list, after='', word_count={}):
    # Base URL for Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Parameters for the request
    params = {
        'limit': 100,
        'after': after
    }

    # Custom headers to prevent being blocked by Reddit
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code != 200:
        return

    # Parse the JSON response
    data = response.json()
    articles = data['data']['children']

    # Convert word_list to lowercase
    word_list = [word.lower() for word in word_list]

    # Initialize word_count dictionary if it's the first call
    if not word_count:
        word_count = {word: 0 for word in word_list}

    # Process each article title
    for article in articles:
        title = article['data']['title'].lower()
        words_in_title = title.split()
        for word in word_list:
            word_count[word] += words_in_title.count(word)

    # Check if there's a next page
    after = data['data']['after']
    if after:
        return count_words(subreddit, word_list, after, word_count)

    # Filter out words with zero counts
    filtered_word_count = {k: v for k, v in word_count.items() if v > 0}

    # Sort the results by count (descending) and alphabetically
    sorted_word_count = sorted(filtered_word_count.items(),
                               key=lambda item: (-item[1], item[0]))

    # Print the results
    for word, count in sorted_word_count:
        print(f"{word}: {count}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format
              (sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
