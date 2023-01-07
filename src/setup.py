import configparser
import json
import os

from src.reddit_auth import reddit_login


class Setup:
    root_path = ''
    config_path = ''
    image_history_path = ''

    def __init__(self, root_path, config_path, image_history_path):
        self.root_path = root_path
        self.config_path = config_path
        self.image_history_path = image_history_path

        self.create_files()

        self.file_obj = open(self.config_path, 'r+')  # open the config.json
        self.settings = json.load(self.file_obj)  # load the JSON data from the file
        self.authenticate()

    def create_files(self):
        # create root directory if not exists
        if not os.path.exists(self.root_path):
            os.makedirs(self.root_path)
        # create config.json and load empty data
        if not os.path.exists(self.config_path):
            data = {
                'client_id': None,
                'client_secret': None,
                'refresh_token': None,
                'subreddit_list': ['wallpaper', 'wallpapers'],
                'download_path': None
            }
            with open(self.config_path, 'w') as outfile:
                json.dump(data, outfile)

        if not os.path.exists(self.image_history_path):
            data = {}  # input an empty list
            with open(self.image_history_path, 'w') as outfile:
                json.dump(data, outfile)

        print("Created required folders")

    def authenticate(self):
        if self.settings['refresh_token'] is None:
            print("No token detected")

            # enter the client details
            self.settings['client_id'] = input('Enter client id \nfound on https://www.reddit.com/prefs/apps\n:')
            self.settings['client_secret'] = input('Enter client secret \nfound on https://www.reddit.com/prefs/apps\n:')

            tmp = reddit_login(self.settings['client_id'],
                               self.settings['client_secret'])  # authorise using reddit_auth.py
            if tmp != 1:  # check if function returns 1(error) or token
                self.settings['refresh_token'] = tmp  # assign the token
                json.dump(self.settings, self.file_obj)  # write to file
                self.file_obj.close()
            else:
                print("Could not get reddit login token")
                print("Exiting")
                quit(-1)
