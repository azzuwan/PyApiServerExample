from japronto import Application
from services.articles import ArticleService

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
app.run(debug=True)
host = 'mongodb://azzuwan:Reddoor74@aws-ap-southeast-1-portal.0.dblayer.com:15501/news'
connect('news',host=host, alias='default')