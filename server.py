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

app = Application()
app.router.add_route('/', index)
app.router.add_route('/articles', articles)
app.router.add_route('/articles/keyword/{keywords}', keywords)
app.run(debug=True)