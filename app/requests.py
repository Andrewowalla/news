import urllib.request, json
from .models import news_source

#getting api key
api_key = none
#getting the news base url
base_url = none

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url =app.config['NEWS_API_BASE_URL']