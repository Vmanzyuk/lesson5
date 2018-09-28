from datetime import datetime

from flask import Flask,abort,request

from req1 import get_weather
from news_list import all_news

import requests
import settings


city_id = 524901

app = Flask(__name__)


@app.route("/")

def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?id={}&APPID={}&units=metric'.format(city_id,settings.API_key)
    weather = get_weather(url,settings.PROXY)
    cur_date = datetime.now().strftime('%d.%m.%Y')
    

    res = '<p><b>Temperature is: {} celcium </b></p>'.format(weather['main']['temp'])
    res += '<p><b>City:{}</b></p>'.format(weather['name'])
    res += '<p><b>date: {}</b></p>'.format(cur_date)
    return res


@app.route('/news')

def all_the_news():
    colors=['green','yellow','blue','red']
    try:
        limit = int(request.args.get('limit'))
    except:
        limit='wrong number'
    color = request.args.get('color') if request.args.get('color') in colors else 'black' 
    return '<h1 style="color: %s">News:<small>%s</small></h1>' % (color,limit)

@app.route('/news/<int:news_id>')

def news_by_id(news_id):
    news_to_show = [news for news in all_news if news['id']==news_id]
    if len(news_to_show)==1:
        result = '<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>'
        result = result % news_to_show[0]
        return result
    else:
        abort(404)


if __name__=='__main__':
    app.run()