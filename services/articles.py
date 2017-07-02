from models.news import Articles

class ArticleService(object):
	def all(self):
		return Articles.objects

	def by_id(self, id):		
		return Articles.objects(id=id)
	
	def keywords(self, keyword):
		return Articles.objects.search_text(keyword).order_by('$text_score')		
		
