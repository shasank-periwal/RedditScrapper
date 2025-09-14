from etls.reddit_etl import connect_reddit, extract_post
from utils.constants import CLIENT_ID, SECRET


def redditpipeline(filename: str, subreddit: str, timefilter = 'day', limit=None):
    instance = connect_reddit(CLIENT_ID, SECRET, 'Shasank Agent')
    posts = extract_post(instance, subreddit, timefilter, limit)
    return posts