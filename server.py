from japronto import Application
from services.articles import ArticleService
from mongoengine import *

article_service = ArticleService()

def index(req):
	"""
	The main index
	"""
	return  req.Response(text='You reached the index!')

def articles(req):
	"""
	Get alll articles
	"""
	#AsyncIO transport buffer problem
	# b_size = req.transport.get_write_buffer_limits()
	# print("Transport Buffer Size: " + str(b_size))
	# req.transport.set_write_buffer_limits(high=131070)
	# b_size = req.transport.get_write_buffer_limits()
	# print("Transport Buffer Size After: " + str(b_size))


	docs = article_service.all()	
	return req.Response(text=docs.to_json())

def keywords(req):
	"""
	Retrieve articles by keywords
	"""
	#AsyncIO buffer problem
	# b_size = req.transport.get_write_buffer_limits()
	# print("Transport Buffer Size: " + str(b_size))
	# req.transport.set_write_buffer_limits(high=131070)
	# b_size = req.transport.get_write_buffer_limits()
	# print("Transport Buffer Size Afteer: " + str(b_size))

	words =  req.match_dict['keywords']	
	docs = article_service.keywords(words)	
	headers = {'Content-Type': 'application/json'}
	body = docs.to_json().encode()	
	return req.Response(body=body, headers=headers)

app = Application()
app.router.add_route('/', index)
app.router.add_route('/articles', articles)
app.router.add_route('/articles/keywords/{keywords}', keywords)

#Some bugs require us to dial to MongoDB just before server is listening
host = 'mongodb://aws-ap-southeast-1-portal.0.dblayer.com/news'
connect(db='news',host=host, port=15501, username='azzuwan', password='Reddoor74', alias='default', connect=False)
app.run(debug=True)