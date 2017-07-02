from japronto import Application
from services.articles import ArticleService
from mongoengine import *

article_service = ArticleService()

def index(req):
	return  req.Response(text='You reached the index!')

def articles(req):
	docs = article_service.all()	
	return req.Response(text=docs.to_json())

def keywords(req):
	words =  req.match_dict["keywords"]
	docs = article_service.keywords(words)
	return req.Response(text=docs.to_json(), headers={"Content-Type", "application/json"})

app = Application()
app.router.add_route('/', index)
app.router.add_route('/articles', articles)
app.router.add_route('/articles/keywords/{keywords}', keywords)
print("FFFFFFFFFF")
# host = 'mongodb://azzuwan:Reddoor74@aws-ap-southeast-1-portal.0.dblayer.com:15501/news'
host = 'mongodb://aws-ap-southeast-1-portal.0.dblayer.com/news'
connect(db='news',host=host, port=15501, username='azzuwan', password='Reddoor74', alias='default', connect=False)
app.run(debug=True)