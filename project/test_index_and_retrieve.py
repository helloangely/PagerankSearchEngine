import unittest
import index
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


class TestIndex(unittest.TestCase):

	def test_bye_stopwords(self):
		should_equal = ['In', 'large', 'bowl', ',', 'beat', 'pumpkin', 'evaporated', 'milk', ',', 'eggs', ',', 'brown', 'sugar', ',', 'cinnamon', ',', 'ginger', ',', 'nutmeg', 'salt', 'electric', 'mixer', 'immersion', 'blender', '.', 'Mix', 'well', '.', 'Pour', 'prepared', 'crust', '.', 'Bake', 'forty', 'minutes', 'knife', 'inserted', '1', 'inch', 'edge', 'comes', 'clean', '.']
		txt = "In a large bowl, beat pumpkin with evaporated milk, eggs, brown sugar, cinnamon, ginger, nutmeg and salt with an electric mixer or immersion blender. Mix well. Pour into a prepared crust. Bake forty minutes or until when a knife is inserted 1 inch from the edge comes out clean."
		tokenized = word_tokenize(txt)
		gowords = index.bye_stopwords(tokenized)
		self.assertEqual(gowords,should_equal)

	def test_stemmer(self):
		should_equal = [u'In', u'larg', u'bowl', u',', u'beat', u'pumpkin', u'evapor', u'milk', u',', u'egg', u',', u'brown', u'sugar', u',', u'cinnamon', u',', u'ginger', u',', u'nutmeg', u'salt', u'electr', u'mixer', u'immers', u'blender', u'.', u'Mix', u'well', u'.', u'Pour', u'prepar', u'crust', u'.', u'Bake', u'forti', u'minut', u'knife', u'insert', u'1', u'inch', u'edg', u'come', u'clean', u'.']
		txt = "In a large bowl, beat pumpkin with evaporated milk, eggs, brown sugar, cinnamon, ginger, nutmeg and salt with an electric mixer or immersion blender. Mix well. Pour into a prepared crust. Bake forty minutes or until when a knife is inserted 1 inch from the edge comes out clean."
		tokenized = word_tokenize(txt)
		gowords = index.bye_stopwords(tokenized)
		stemmed = index.stemmer(gowords)
		self.assertEqual(stemmed,should_equal)

	def test_update_inverted_index(self):
		should_equal = {u'brown': [['doc1', 1]], u'edg': [['doc1', 1]], u'insert': [['doc1', 1]], u'beat': [['doc1', 1]], u'crust': [['doc1', 1]], u'In': [['doc1', 1]], u'ginger': [['doc1', 1]], u'Mix': [['doc1', 1]], u'Pour': [['doc1', 1]], u'sugar': [['doc1', 1]], u'come': [['doc1', 1]], u'milk': [['doc1', 1]], u'blender': [['doc1', 1]], u'well': [['doc1', 1]], u'evapor': [['doc1', 1]], u'salt': [['doc1', 1]], u'prepar': [['doc1', 1]], u'immers': [['doc1', 1]], u'bowl': [['doc1', 1]], u',': [['doc1', 6]], u'mixer': [['doc1', 1]], u'.': [['doc1', 4]], u'1': [['doc1', 1]], u'nutmeg': [['doc1', 1]], u'cinnamon': [['doc1', 1]], u'clean': [['doc1', 1]], u'electr': [['doc1', 1]], u'inch': [['doc1', 1]], u'larg': [['doc1', 1]], u'minut': [['doc1', 1]], u'Bake': [['doc1', 1]], u'egg': [['doc1', 1]], u'forti': [['doc1', 1]], u'knife': [['doc1', 1]], u'pumpkin': [['doc1', 1]]}
		inverted_index = {}
		txt = "In a large bowl, beat pumpkin with evaporated milk, eggs, brown sugar, cinnamon, ginger, nutmeg and salt with an electric mixer or immersion blender. Mix well. Pour into a prepared crust. Bake forty minutes or until when a knife is inserted 1 inch from the edge comes out clean."
		tokenized = word_tokenize(txt)
		gowords = index.bye_stopwords(tokenized)
		stemmed = index.stemmer(gowords)
		index.update_inverted_index(stemmed, inverted_index, "doc1")
		self.assertEqual(inverted_index,should_equal)
	
	def test_get_links_html(self):
		html_txt = '<!DOCTYPE html><html><head><title>Page Title</title></head></html>'
		t = index.get_links_html(html_txt)
		self.assertEqual(t,'Page Title')
	
if __name__ == '__main__':
    unittest.main()