class Sources:
    '''
    news_source class to define news source objects
    '''
    def __init__(self,id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
  

class Articles:
    '''
    news_article class to define news article objects
    '''
    def __init__(self,source, author, description, publishedAt ,url, urlToImage, title):
        self.source = source
        self.author = author
        self.description = description
        self.publishedAt = publishedAt
        self.url = url
        self.urlToImage = urlToImage
        self.title = title
