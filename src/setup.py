import configparser
import json
import os

from src.reddit_auth import reddit_login


def create_files(root_path, config_path, wallpaper_list_path):
    # create root directory if not exists
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    # create config.json and load empty data
    if not os.path.exists(config_path):
        data = {
            'client_id': None,
            'client_secret': None,
            'refresh_token': None,
            'subreddit_list': ['wallpaper', 'wallpapers'],
            'download_path': None
        }
        with open(config_path, 'w') as outfile:
            json.dump(data, outfile)

    if not os.path.exists(wallpaper_list_path):
        data = {}  # input an empty list
        with open(wallpaper_list_path, 'w') as outfile:
            json.dump(data, outfile)

    print("Created required folders")


def load_clientid():
    # Read the credentials from the INI file
    conf = configparser.ConfigParser()
    conf.read('secret.ini')
    return [conf['reddit']['client_id'], conf['reddit']['client_secret']]


def authenticate(config_path):
    with open(config_path, 'r+') as con:
        settings = json.load(con)
        if len(settings['refresh_token']) == 0:
            print("No token detected")
            tmp = reddit_login(load_clientid())  # authorise using reddit_auth.py
            if tmp != 1:  # check if function returns 0 or token
                settings['refresh_token'] = tmp  # assign the token
                json.dump(settings, con)  # write to file
            else:
                print("Could not get reddit login token")
                print("Exiting")
                quit(-1)


def run_setup():
    create_files()
    authenticate()
