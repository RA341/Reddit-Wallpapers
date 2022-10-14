import os
import time
import praw
from file_functions import dumpPickle, readPickle, dumpSubreddit, readSubreddits
import tkinter as tk
from tkinter import filedialog
import urllib.request

# folder = 'data'
# if not os.path.exists(folder):
#     os.makedirs(folder)

reddit = praw.Reddit(
    client_id='63NRVVv_imYBeWE9Dwb-eg',
    client_secret=None,
    refresh_token=readPickle('refresh_token.pickle'),
    user_agent='A app to download wallpapers',
)


def getSavedWallpapers():
    subreddits = readSubreddits('subreddits.txt')
    post_dict = {}
    downloaded_dict = readPickle('downloaded_wallpaper.pickle')

    print("Previously downloaded list:\n", downloaded_dict)
    tmp = []
    saved = []
    start = time.perf_counter()
    try:
        saved = list(reddit.user.me().saved(limit=None))
        print('Successfully received saved posts')
        print("There are ", len(saved), "saved posts")
    except Exception as e:
        print('failure to get saved posts')
        print(e)
        quit(-1)

    try:
        for item in saved:
            if str(item.subreddit) in subreddits:
                if not item.is_self:
                    try:
                        if item.is_gallery:
                            for i in list(item.media_metadata):
                                tmp.append(item.media_metadata[i]['s']['u'].replace('preview', 'i').split('?')[0])
                            if not downloaded_dict.get(item.id):
                                downloaded_dict.update({item.id: item.url})
                                post_dict[item.id] = tmp
                                print("Adding ", item.id)
                            else:
                                print("Skipping already downloaded ", item.id)
                    except Exception:
                        # print("Not a Gallery")
                        if not downloaded_dict.get(item.id):
                            downloaded_dict.update({item.id: item.url})
                            post_dict[item.id] = item.url
                            print("Adding ", item.id)
                        else:
                            print("Skipping already downloaded ", item.id)
    except Exception as e:
        print("curses", e)

    stop = time.perf_counter()

    print("time taken ", stop - start)
    print("Found", len(post_dict), "saved posts from matching subreddits")
    dumpPickle('downloaded_wallpaper.pickle', downloaded_dict)

    return post_dict


if __name__ == '__main__':
    folder = 'data'
    if not os.path.exists(folder):
        os.makedirs(folder)

    post_dict = getSavedWallpapers()

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    file_path = file_path + "/"
    for key in post_dict.keys():
        link = post_dict.get(key)
        if type(link) == list:
            for index, data in enumerate(link):
                print('downloading ', index, key + '.jpg')
                try:
                    urllib.request.urlretrieve(data, file_path + '_{}'.format(key) + '{}.jpg'.format(index))
                except Exception as e:
                    print("failed to download", key + '.jpg')
                    print(e)
        else:
            print('downloading ', key + '.jpg')
            try:
                urllib.request.urlretrieve(link, file_path + "{}.jpg".format(key))
            except Exception as e:
                print("failed to download", key + '.jpg')
                print(e)
