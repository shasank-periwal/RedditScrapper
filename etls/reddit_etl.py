from praw import Reddit

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