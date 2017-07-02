from mongoengine import *

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