import requests 
from datetime import datetime

# Define the Feed EP on Wikipedia
FEED_ENDPOINT = "https://en.wikipedia.org/api/rest_v1/feed/featured/"

# Get today's date from python's datetime library
today = datetime.today()
year, month, day = today.year, today.month, today.day

def build_feed_request(feed_ep = FEED_ENDPOINT, year = today.year, month = today.month, day = today.day):
    """ Input: Feed end point, year as int, month as int, day as int
    Output: Composed request URL"""

    request_url = feed_ep + str(year) + "/" + str(month) + "/" + str(day)
    return(request_url)

def make_request():
    r = requests.get(build_feed_request())
    return(r)

# TFA is the code that wikipedia gives to today's featured article
featured_article = make_request().json()["tfa"]

title = featured_article["displaytitle"]
image = featured_article["thumbnail"]["source"]
summary = featured_article["extract"]


