# reddit-image-downloader
I love the wallpapers shared on the [r/wallpaper](https://www.reddit.com/r/wallpaper/) and [r/wallpapers](https://www.reddit.com/r/wallpapers/), so I created this script to download wallpapers automatically.

* Save the post on reddit.
* Run the script.
* The script will automatically download the images to a folder of your choice.

# Pre-Requisite
* [Python installation](https://www.tutorialspoint.com/how-to-install-python-in-windows) (added to path)
* Get the ```client_id``` and ```client_secret``` from the [reddit api](https://www.reddit.com/prefs/apps) ([follow this guide](https://redditclient.readthedocs.io/en/latest/oauth/)) 

# Installation
* Download the ```src``` directory and ```requirments.txt```
* Open cmd/powershell/terminal 
* Install required libraries by ```pip install -r requirments.txt``` 


# Usage
* run script using ```python (path to file)/main.py```.
* In your preferences folder add your preferred subreddits in ```config.json``` in the ```subreddit_list``` section.

## Note
* You need to be logged in to reddit on your default browser.
* If you are not logged in the script won't be able to get the details it needs.




