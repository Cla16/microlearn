import requests 
from datetime import datetime

# Define the Feed EP on Wikipedia
FEED_ENDPOINT = "https://en.wikipedia.org/api/rest_v1/feed/featured/"

# Get today's date from python's datetime library
today = datetime.today()
year, month, day = today.year, today.month, today.day

def build_feed_request(feed_ep = FEED_ENDPOINT):
    """ Input: Feed end point, year as int, month as int, day as int
    Output: Composed request URL"""
    today = datetime.today()
    year, month, day = today.year, today.month, today.day
    request_url = feed_ep + str(year) + "/" + str(month) + "/" + str(day)
    return(request_url)

def make_request():
    r = requests.get(build_feed_request())
    return(r)

def parse_request():
    r = make_request()
    
    # TFA is the code that wikipedia gives to today's featured article
    featured_article = make_request().json()["tfa"]
    
    title = featured_article["title"].replace('_', ' ')
    image = featured_article["thumbnail"]["source"]
    # Be sure to replace non breaking spaces with real spaces
    summary = featured_article["extract"].replace('\xa0', ' ')
    url = featured_article["content_urls"]["desktop"]["page"]

    article_data = {
            "title" : title,
            "image" : image,
            "summary" : summary,
            "url" : url
            }
    return(article_data)
