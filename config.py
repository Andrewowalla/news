import os

class config:
    
    NEWS_API_BASE_URL='https://api.newsapi.org/3/news/{}?api_key={4030fb45887646ea8e7d53b82646d351}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    SECRET_KEY=

class ProdConfig(config):
    pass

class DevConfig(config):
    DEBUG=True

config_options={
    'development'=DevConfig,
    'production'=ProdConfig
}