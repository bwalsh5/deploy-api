import os

from pynytimes import NYTAPI
# This is the API Key we setup and added to the env earlier
nyt = NYTAPI("C13CgQOrQnPVAraBFr0A305SgrCY9jef", parse_dates=True)

def get_top_stories():
    return nyt.top_stories()