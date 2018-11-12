from flask import Flask, render_template, request
import feedparser


app = Flask(__name__)
app.config['DEBUG'] = True

RSS_FEEDS = {
  'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
  'cnn': 'http://rss.cnn.com/rss/edition.rss',
  'fox': 'http://feeds.foxnews.com/foxnews/latest',
  'iol': 'http://www.iol.co.za/cmlink/1.640'
}


@app.route('/')
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = 'bbc'
    else:
        publication = query.lower()
