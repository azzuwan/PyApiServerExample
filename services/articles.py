from models.news import Articles

class ArticleService(object):
	def all(self):
		"""
		Get all news articles
		"""
		return Articles.objects

	def by_id(self, id):
		"""
		Get article by it's Mongo ID
		"""	
		return Articles.objects(id=id)
	
	def keywords(self, keyword):
		"""
		Get articles based on keywords and full text search
		and sort them by accuracy ranking
		"""
		return Articles.objects.search_text(keyword).order_by('$text_score')		

		
