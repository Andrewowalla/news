class news_source:
    '''
    news_source class to define news source objects
    '''
    def __init__(self, id, name):
        self.id = id
        self.name = name

class news_article:
    '''
    news_article class to define news article objects
    '''
    def __init__(self, title, description, url, urlToImage, content, publishedAt):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt = publishedAt