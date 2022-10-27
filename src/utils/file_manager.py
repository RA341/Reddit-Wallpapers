import pickle
import os

# Worker folder paths
# WARNING DO NOT CHANGE THESE UNLESS YOU KNOW WHAT YOU ARE DOING
data_folder = './preferences'
subreddits_file = './subreddits.txt'
old_wallpaper_list = './' + data_folder[2:] + '/downloaded_wallpaper.pickle'
token_path = './' + data_folder[2:] + '/refresh_token.pickle'


def createFiles():
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
        dumpPickle(token_path, '')
        dumpPickle(old_wallpaper_list, {})
        f = open('./lists/download_path.txt', 'w')
        f.write('')
        print("Created required folders")


def dumpPickle(filepath, post_dict):
    with open(filepath, 'wb') as handle:
        pickle.dump(post_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


def readPickle(filepath):
    with open(filepath, 'rb') as handle:
        return pickle.load(handle)


def dumpSubreddit(filepath, sub_list):
    with open(filepath, 'w') as f:
        for x in sub_list:
            f.write(x + '\n')


def readSubreddits(filepath):
    tmp = []
    with open(filepath, 'r') as f:
        for x in f.readlines():
            s = x.strip()
            if len(s) == 0:
                continue
            if s[0] not in ['/']:
                tmp.append(s)
    return tmp
