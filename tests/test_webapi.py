import sys, os, unittest, datetime
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from services.articles import ArticleService
from pprint import pprint
import requests


class WebApiTest(unittest.TestCase):
	def test_keywords(self):
		r = requests.get('https://localhost:8080/articles/keywords/singapore')
		self.assertTrue(if 'singapore' in r.text)


