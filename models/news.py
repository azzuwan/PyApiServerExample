from mongoengine import *

host = 'mongodb://azzuwan:Reddoor74@aws-ap-southeast-1-portal.2.dblayer.com:15501,aws-ap-southeast-1-portal.0.dblayer.com:15501/news'
connect(host=host)

class Articles(Document):
	# The title of the news article
	title = StringField(required=True)
	# News content	
	body = StringField(required=True)
	# Publication date
	published = DateTimeField()
	# Article author 
	author = StringField()
	# Category tags
	tags = ListField(StringField())
	# News agency name
	agency = StringField(required=True)
	# Original URL of the article
	url = StringField(required=True)