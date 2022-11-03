import os
import time
import praw
from tkinter import filedialog
import requests

from modules.file_manager import dumpPickle, readPickle, readSubreddits, createFiles, subreddits_file, \
    old_wallpaper_list, data_folder
from modules.reddit_auth import redditAuthCheck


def getSavedImages(reddit, downloaded_images):
    print("Initializing please wait....")

    subreddits = readSubreddits(subreddits_file)

    if not len(subreddits):
        print("Error no subreddits detected")
        print("Add your subreddits in", subreddits_file)
        quit(-1)

    post_list = {}

    tmp = []
    saved = []
    start = time.perf_counter()

    print("Getting saved posts")
    try:
        saved = list(reddit.user.me().saved(limit=None))
        print('Successfully received saved posts')
        print("There are ", len(saved), "saved posts\n")
    except Exception as e:
        print('failure to get saved posts\n')
        print(e)
        quit(-1)

    try:
        print("Filtering posts")
        for item in saved:
            if str(item.subreddit) in subreddits:
                if not item.is_self:
                    try:
                        if item.is_gallery:
                            for i in list(item.media_metadata):
                                tmp.append(item.media_metadata[i]['s']['u'].replace('preview', 'i').split('?')[0])
                            if not downloaded_images.get(item.id):
                                post_list[item.id] = tmp
                                print("Adding ", item.id)
                            else:
                                if post_list[item.id] == tmp:
                                    print("Skipping", item.id, 'already downloaded')
                                else:
                                    diff = set(tmp) - set(post_list[item.id])
                                    post_list[item.id] = list(diff)
                                    print("Adding ", item.id)
                            tmp = []  # resetting gallery image list
                    except Exception:
                        # Not a Gallery
                        if not downloaded_images.get(item.id):
                            post_list[item.id] = item.url
                            print("Adding ", item.id)
                        else:
                            print("Skipping", item.id, 'already downloaded')
    except Exception as e:
        print("curses", e)

    stop = time.perf_counter()

    print("\nFound", len(post_list), "new saved posts from matching subreddits")
    print("time taken ", round(stop - start), 's\n')

    return post_list


def downloadImage(url: str, filepath: str) -> requests.models.Response:
    r = requests.get(url)
    with open(filepath, 'wb') as f:
        f.write(r.content)
    f.close()
    return r


def imageDownloader(post_list, downloaded_images):
    if not len(post_list.keys()):
        print("All images are downloaded\nNothing to download\nExiting")
        quit(2)
    success = 0
    failed = 0
    total = 0

    with open( data_folder+'/download_path.txt', 'r') as d:
        download_path = d.read()
    if not len(download_path):
        print("\nPlease select download folder in the dialog\n")
        file_path = filedialog.askdirectory() + "/"
        open(data_folder + '/download_path.txt', 'w').write(file_path)
        download_path = file_path
    else:
        print("Found previous download path\n")
        print(download_path)
        print("You can change it at", os.path.abspath(data_folder + '/download_path.txt'), '\n')
    start = time.perf_counter()
    for key in post_list.keys():
        link = post_list.get(key)
        if type(link) == list:
            tmp = []
            for index, data in enumerate(link):
                print('downloading', key, str(index + 1) + '.png')
                total += 1
                response = downloadImage(data, download_path + '{}_'.format(key) + '{}.png'.format(index + 1))
                if response.ok:
                    tmp.append(data)
                    success += 1
                #     print('downloaded', key, str(index + 1) + '.png')
                else:
                    failed += 1
                    print("failed to download", key, str(index + 1) + '.png')
                    print("Response", response.status_code + ":" + response.reason)

            t = downloaded_images.get(key)
            if not t:
                downloaded_images.update({key: tmp})
            else:
                downloaded_images[key] = t.extend(tmp)
        else:
            print('downloading', key + '.png')
            total += 1
            response = downloadImage(link, download_path + "{}.png".format(key))
            if response.ok:
                downloaded_images.update({key: link})
                success += 1
                # print('downloaded', key + '.png')
            else:
                failed += 1
                print("failed to download", key + '.png')
                print(e)
        time.sleep(0.5)

    dumpPickle(old_wallpaper_list, downloaded_images)
    stop = time.perf_counter()
    print("\nFinished in", round(stop - start), 's')
    print("Downloaded", success, 'images', 'out of', total)
    if failed:
        print("Failed to download", failed, 'images', 'out of', str(total) + "\n")


if __name__ == '__main__':
    createFiles()
    try:
        token = redditAuthCheck()
    except Exception as e:
        print("Error getting token")
        print(e)
        quit(-1)

    reddit = praw.Reddit(
        client_id='63NRVVv_imYBeWE9Dwb-eg',
        client_secret=None,
        refresh_token=token,
        user_agent='A src to download wallpapers',
    )
    downloaded_images = readPickle(old_wallpaper_list)
    posts = getSavedImages(reddit, downloaded_images)
    imageDownloader(posts, downloaded_images)
