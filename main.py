import os
import time
import praw
from file_functions import dumpPickle, readPickle, dumpSubreddit, readSubreddits

folder = 'data'
if not os.path.exists(folder):
    os.makedirs(folder)


reddit = praw.Reddit(
    client_id='63NRVVv_imYBeWE9Dwb-eg',
    client_secret=None,
    refresh_token=readPickle('refresh_token.pickle'),
    user_agent='A app to download wallpapers',
)

subreddits = readSubreddits('subreddits.txt')

if __name__ == '__main__':
    os.mkdir('data')
    post_dict = {}

    downloaded_dict = readPickle('downloaded_wallpaper.pickle')

    start = time.perf_counter()
    tmp = []

    try:
        for item in reddit.user.me().saved(limit=None):
            submission = reddit.submission(id=item.id)
            if str(submission.subreddit) in subreddits:
                if submission.is_self is not True:
                    try:
                        if submission.is_gallery:
                            print("Gallery")
                            for i in list(submission.media_metadata):
                                tmp.append(submission.media_metadata[i]['s']['u'].replace('preview', 'i').split('?')[0])
                            if not downloaded_dict.get(submission.id):
                                downloaded_dict.update(submission.id, tmp)
                                post_dict[submission.id] = tmp
                            print("Adding ", submission.id)
                    except Exception:
                        print("No gallery")
                        if downloaded_dict.get(submission.id):
                            downloaded_dict.update(submission.id, submission.url)
                            post_dict[submission.id] = submission.url
                        print("Adding ", submission.id)

    except Exception as e:
        print(e)

    stop = time.perf_counter()

    print("time taken ", stop - start)
    print("link post_dict", post_dict)
    dumpPickle('downloaded_wallpaper.pickle', downloaded_dict)
    dumpSubreddit('subreddits.txt', subreddits)
