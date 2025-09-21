from etls.reddit_etl import connect_reddit, extract_post, load_data_to_csv, transform_data
from utils.constants import CLIENT_ID, OUTPUT_PATH, SECRET
import pandas as pd

def redditpipeline(filename: str, subreddit: str, timefilter = 'day', limit=None):
    instance = connect_reddit(CLIENT_ID, SECRET, 'Shasank Agent')
    posts = extract_post(instance, subreddit, timefilter, limit)

    post_df = pd.DataFrame(posts)
    post_df = transform_data(post_df)

    file_path = f"{OUTPUT_PATH}/{filename}.csv"
    load_data_to_csv(post_df, file_path)

    return file_path