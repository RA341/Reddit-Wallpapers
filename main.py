import os
import time
import praw
from file_functions import dumpPickle, readPickle, dumpSubreddit, readSubreddits, createFolders
import tkinter as tk
from tkinter import filedialog
import urllib.request

try:
    token = readPickle('./data/refresh_token.pickle')
except Exception as e:
    print("Error getting token")
    print(e)
    quit(-1)

reddit = praw.Reddit(
    client_id='63NRVVv_imYBeWE9Dwb-eg',
    client_secret=None,
    refresh_token=token,
    user_agent='A app to download wallpapers',
)


def getSavedWallpapers(reddit):
    print("Initializing please wait....")
    subreddits_file = './data/subreddits.txt'
    downloaded_wallpapers = './data/downloaded_wallpaper.pickle'

    subreddits = readSubreddits(subreddits_file)
    post_list = {}
    downloaded_images = readPickle(downloaded_wallpapers)

    tmp = []
    saved = []
    start = time.perf_counter()
    try:
        saved = list(reddit.user.me().saved(limit=None))
        print('Successfully captured saved posts')
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
                            if not downloaded_images.get(item.id):
                                downloaded_images.update({item.id: tmp})
                                post_list[item.id] = tmp
                                print("Adding ", item.id)
                            else:
                                print("Skipping", item.id, 'already downloaded')
                            tmp = []  # resetting gallery image list
                    except Exception:
                        # Not a Gallery
                        if not downloaded_images.get(item.id):
                            downloaded_images.update({item.id: item.url})
                            post_list[item.id] = item.url
                            print("Adding ", item.id)
                        else:
                            print("Skipping", item.id, 'already downloaded')
    except Exception as e:
        print("curses", e)

    stop = time.perf_counter()

    print("time taken ", stop - start)
    print("Found", len(post_list), "new saved posts from matching subreddits")
    print("Previously downloaded list:\n", downloaded_images)
    dumpPickle(downloaded_wallpapers, downloaded_images)

    return post_list


def downloadWallpapers(post_list):
    if len(post_list.keys()) == 0:
        print("Empty list\nNothing to download\nExiting")
        quit(-1)
    images = 0
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory() + "/"
    for key in post_list.keys():
        link = post_list.get(key)
        if type(link) == list:
            for index, data in enumerate(link):
                print('downloading', key, str(index + 1) + '.png')
                try:
                    urllib.request.urlretrieve(data, file_path + '{}_'.format(key) + '{}.png'.format(index + 1))
                    images += 1
                except Exception as e:
                    print("failed to download", key, str(index + 1) + '.png')
                    print(e)
        else:
            print('downloading ', key + '.png')
            try:
                urllib.request.urlretrieve(link, file_path + "{}.png".format(key))
                images += 1
            except Exception as e:
                print("failed to download", key + '.png')
                print(e)
    print("Finished")
    print("downloaded", images, 'images')


if __name__ == '__main__':

    createFolders()

    posts = getSavedWallpapers(reddit)

    downloadWallpapers(posts)
