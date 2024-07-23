from flask import Flask, render_template, request
import requests
from config import WHEATHER_API_KEY, NEWS_API_KEY

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    quote = None
    weather = None
    news = None
    if request.method == 'POST':
        city = request.form['city']
        #weather = get_weather(city)
        news = get_news()
        quote = get_random_quotes()
    return render_template("index.html", weather=weather, quote = quote, news = news)

def get_weather(city):
    api_key = WHEATHER_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    return response.json()


def get_news():
    api_key = NEWS_API_KEY
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get('articles', [])

def get_random_quotes():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    return response.json()

'''
    {
        "_id": "Aya0eLpghjxG",
        "content": "The purpose of learning is growth, and our minds, unlike our bodies, can continue growing as we continue to live.",
        "author": "Mortimer J. Adler",
        "tags": [
            "Famous Quotes"
        ],
        "authorSlug": "mortimer-j-adler",
        "length": 113,
        "dateAdded": "2019-09-13",
        "dateModified": "2023-04-14"
    }
'''

if __name__ == '__main__':
    app.run(debug=True)
