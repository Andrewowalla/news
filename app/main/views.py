from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get news
from app import app

#views
@ main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    news = get_news()
    title = 'MAZ NEWS'
    return render_template('index.html', title = title )
    