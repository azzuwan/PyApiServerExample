import sys, os, unittest, datetime
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from services.articles import ArticleService
from pprint import pprint

class ArticleServiceTest(unittest.TestCase):
	service = ArticleService()
	def test_all(self):
		articles = self.service.all()
		for article in articles:
			pprint(article.title)
		size = len(articles)
		self.assertTrue(size > 0)

	def test_keyword(self, keyword='Test'):
		articles = self.service.keyword(keyword)
		for article in articles:
			pprint(article.title)
		size = len(articles)
		self.assertTrue(size > 0)


if __name__ == '__main__':
    unittest.main()