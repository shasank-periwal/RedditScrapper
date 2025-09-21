from praw import Reddit
import pandas as pd
import numpy as np
from utils.constants import POST_FIELDS 

def connect_reddit(client_id: str, secret: str, agent_name: str) -> Reddit:
    try:
        reddit = Reddit(client_id = client_id, client_secret = secret, user_agent = agent_name)
        print("Connected")
        return reddit 
    except Exception as e:
        print("Could not connect")
        print(e)

def extract_post(instance: Reddit, subreddit: str, timefilter: str, limit=None):
    sub_reddit = instance.subreddit(subreddit)
    posts = sub_reddit.top(time_filter=timefilter, limit = limit)

    post_list = []

    for post in posts:
        post_dict = vars(post)
        post = {key: post_dict[key] for key in POST_FIELDS}
        post_list.append(post)
    
    return post_list

def transform_data(df: pd.DataFrame):
    df['created_at'] = pd.to_datetime(df["created_utc"])
    df['over_18'] = np.where((df['over_18'] == True), True, False)
    df['author'] = df['author'].astype(str)
    edited_mode = df['edited'].mode()
    df['edited'] = np.where(df['edited'].isin([True, False]),
                                 df['edited'], edited_mode).astype(bool)
    df['num_comments'] = df['num_comments'].astype(int)
    df['score'] = df['score'].astype(int)
    df['title'] = df['title'].astype(str)
    return df

def load_data_to_csv(data: pd.DataFrame, path: str):
    data.to_csv(path, index=False)