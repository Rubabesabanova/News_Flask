from flask import render_template, url_for
from news import app
from news.db import news_list
@app.route('/')
@app.route('/news')
def news():
    return render_template('news.html', data=news_list)

@app.route('/news/<id>')
def single_news(id):
    return render_template('news.html', data=news_list, news_id=id)