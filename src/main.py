import json
import os
import time

import praw
import prawcore
import requests

from setup import Setup

# folder paths :
# WARNING DO NOT CHANGE THESE UNLESS YOU KNOW WHAT YOU ARE DOING
root = './wall-py'
config = root + '/config.json'
wallpaper_list = root + '/download_history.json'


def get_saved_images(reddit, downloaded_images, config):
    print("Initializing please wait....")
    saved = []

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

    print("Filtering posts...")
    for item in saved:
        if str(item.subreddit) not in subreddits:  # skip if subreddit not in list
            continue
        if item.is_self is True:  # skip if text posts
            continue
        try:
            tmp = []
            if item.is_gallery is False:  # skip if not gallery
                continue
            if downloaded_images.get(item.id) is None:  # add to list if not already added
                for i in list(item.media_metadata):
                    # replace preview link with actual link (preview.reddit -> i.reddit)
                    link = item.media_metadata[i]['s']['u'].replace('preview', 'i').split('?')[0]
                    tmp.append([link, False])  # assign initial download value of false
                downloaded_images[item.id] = tmp
                print("Adding ", item.id)
            else:
                print("Skipping", item.id, 'already added')
        except prawcore.exceptions.InsufficientScope:  # Not a Gallery (received 403 HTTP response)
            if downloaded_images.get(item.id) is None:
                downloaded_images[item.id] = [item.url, False]  # assign initial download value of false
                print("Adding ", item.id)
            else:
                print("Skipping", item.id, 'already added')

    stop = time.perf_counter()

    print("\nFound", len(downloaded_images), "saved posts from matching subreddits")
    print("time taken ", round(stop - start), 's\n')

    with open(wallpaper_list, 'w') as f:
        json.dump(downloaded_images, f)


def download_image(url: str, filepath: str) -> requests.models.Response:
    r = requests.get(url)
    with open(filepath, 'wb') as f:
        f.write(r.content)
    f.close()
    return r


class DownloadManager:
    success, failed, total = 0, 0, 0

    def __init__(self, download_path):
        print('Downloading images...')
        self.download_path = download_path
        with open(wallpaper_list, 'r') as _:
            self.image_list = json.load(_)
        self.main()

    def download_status(self, url, download_path, key):
        self.total += 1
        response = download_image(url, download_path)
        if response.ok:
            self.image_list[key][1] = True
            self.success += 1
        else:
            self.failed += 1
            print("failed to download", key + '.png')
        time.sleep(0.2)

    def filters(self):
        if len(self.image_list.keys()) == 0:  # check if there are any images to download
            print("All images are downloaded\nNothing to download\nExiting")
            quit(0)

        if not len(self.download_path):  # check if download path exits
            print('No download path found please add it in', os.path.abspath(config))
            quit(-1)

    def main(self):
        start = time.perf_counter()
        for key in self.image_list.keys():
            url_list = self.image_list.get(key)
            if isinstance(url_list[0], list):  # if gallery
                for index, data in enumerate(url_list):
                    if data[1] is True:  # skip if already downloaded
                        print(f'Skipping {key} already downloaded')
                        continue
                    print('downloading', key, str(index + 1) + '.png')
                    self.download_status(url_list[0], f"{self.download_path}{key}_{index + 1}.png",
                                         f'{key}_{index + 1}')
            else:
                if url_list[1] is True:  # skip if already downloaded
                    print(f'Skipping {key} already downloaded')
                    continue

                print('downloading', key + '.png')
                self.download_status(url_list[0], f"{self.download_path}{key}.png", key)

        with open(wallpaper_list, 'w') as _:
            json.dump(self.image_list, _)

        stop = time.perf_counter()
        print("\nFinished in", round(stop - start), 's')
        print("Downloaded", self.success, 'images', 'out of', self.total)
        if self.failed is not 0:
            print("self.failed to download", self.failed, 'images', 'out of', str(self.total) + "\n")


if __name__ == '__main__':
    if os.path.exists(config) is False or os.path.exists(wallpaper_list) is False:
        print('Running Setup (this will happen only once)')
        Setup(root, config, wallpaper_list)

    # running the main program
    # open the required files
    with open(config, 'r') as f:  # open the config.json
        config = json.load(f)  # load the JSON data from the file
    with open(wallpaper_list, 'r') as f:  # open the config.json
        downloaded_wallpapers = json.load(f)  # load the JSON data from the file

    reddit = praw.Reddit(
        client_id=config['client_id'],  # read the client_id
        client_secret=config['client_secret'],  # read the client_secret
        refresh_token=config['refresh_token'],
        user_agent='A src to download wallpapers',
    )

    get_saved_images(reddit, downloaded_wallpapers, config)
    DownloadManager(config['download_path'])
