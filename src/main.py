import json
import os
import time

import praw
import requests

from setup import Setup

# folder paths :
# WARNING DO NOT CHANGE THESE UNLESS YOU KNOW WHAT YOU ARE DOING
root = './wall-py'
config = root + '/config.json'
wallpaper_list = root + '/download_history.json'


def get_saved_images(reddit, downloaded_images, config):
    print("Initializing please wait....")
    posts_list = {}
    saved = []

    def extract_gallery():
        tmp = []
        if item.is_gallery:  # check for gallery
            if downloaded_images.get(item.id) is None:  # add to list if not already added
                for i in list(item.media_metadata):
                    # replace preview link with actual link (preview.reddit -> i.reddit)
                    link = item.media_metadata[i]['s']['u'].replace('preview', 'i').split('?')[0]
                    tmp.append({link: False})  # assign initial download value of false
                downloaded_images[item.id] = tmp
                print("Adding ", item.id)
            else:
                print("Skipping", item.id, 'already downloaded')

    subreddits = config['subreddit_list']

    if not len(subreddits):
        print("Warning!!, no subreddits found")
        print("Add your subreddits in", config)
        print('Then run the script again')
        quit(-1)

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
                if item.is_self is False:  # filter out text posts
                    try:
                        extract_gallery()
                    except Exception as e:  # Not a Gallery
                        if downloaded_images.get(item.id) is None:
                            downloaded_images[item.id] = {item.url: False}  # assign initial download value of false
                            print("Adding ", item.id)
                        else:
                            print("Skipping", item.id, 'already downloaded')
    except Exception as e:
        print("curses", e)

    stop = time.perf_counter()

    print("\nFound", len(downloaded_images), "saved posts from matching subreddits")
    print("time taken ", round(stop - start), 's\n')

    print(downloaded_images)
    with open(wallpaper_list, 'w') as f:
        json.dump(downloaded_images, f)


def download_image(url: str, filepath: str) -> requests.models.Response:
    r = requests.get(url)
    with open(filepath, 'wb') as f:
        f.write(r.content)
    f.close()
    return r


# def download_manager(post_list, downloaded_images, download_path):
#     if len(post_list.keys()) == 0:  # check if there are any images to download
#         print("All images are downloaded\nNothing to download\nExiting")
#         quit(2)
#     success = 0
#     failed = 0
#     total = 0
#
#     if not len(download_path):
#         print('No download path found please add it in', os.path.abspath(config))
#
#     start = time.perf_counter()
#     for key in post_list.keys():
#         link = post_list.get(key)
#         if type(link) == list:
#             tmp = []
#             for index, data in enumerate(link):
#                 print('downloading', key, str(index + 1) + '.png')
#                 total += 1
#                 response = download_image(data, download_path + '{}_'.format(key) + '{}.png'.format(index + 1))
#                 if response.ok:
#                     tmp.append(data)
#                     success += 1
#                 #     print('downloaded', key, str(index + 1) + '.png')
#                 else:
#                     failed += 1
#                     print(f"failed to download {key} {str(index + 1)}.png")
#                     print(f'"Response", {response.status_code} + ":" + {response.reason}')
#
#             t = downloaded_images.get(key)
#             if not t:
#                 downloaded_images.update({key: tmp})
#             else:
#                 downloaded_images[key] = t.extend(tmp)
#         else:
#             print('downloading', key + '.png')
#             total += 1
#             response = download_image(link, download_path + "{}.png".format(key))
#             if response.ok:
#                 downloaded_images.update({key: link})
#                 success += 1
#                 # print('downloaded', key + '.png')
#             else:
#                 failed += 1
#                 print("failed to download", key + '.png')
#         time.sleep(0.5)
#
#     with open(config, 'w') as f:
#         json.dump(downloaded_images, f)
#     stop = time.perf_counter()
#     print("\nFinished in", round(stop - start), 's')
#     print("Downloaded", success, 'images', 'out of', total)
#     if failed:
#         print("Failed to download", failed, 'images', 'out of', str(total) + "\n")


if __name__ == '__main__':
    if os.path.exists(config) is False or os.path.exists(wallpaper_list) is False:
        print('Running Setup (this will happen only once)')
        Setup(root, config, wallpaper_list)

    # run script

    # open the required files
    with open(config, 'r') as f:  # open the config.json
        config = json.load(f)  # load the JSON data from the file
    with open(wallpaper_list, 'r') as f:  # open the config.json
        downloaded_wallpapers = json.load(f)  # load the JSON data from the file
    print(downloaded_wallpapers)

    reddit = praw.Reddit(
        client_id=config['client_id'],  # read the client_id
        client_secret=config['client_secret'],  # read the client_secret
        refresh_token=config['refresh_token'],
        user_agent='A src to download wallpapers',
    )

    print(get_saved_images(reddit, downloaded_wallpapers, config))
    # run_downloader(reddit)
