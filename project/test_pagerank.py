import unittest
import pagerank 

class TestIndex(unittest.TestCase):
	def test_pagerank(self):
		
		g = {}
		g["green"] = ["orange", "blue"]
		g["blue"] = ["red", "orange"]
		g["red"] = ["orange", "blue", "green"]

		x = pagerank.pagerank(g)
		shouldEqual = {'blue': 0.15188148148148148, 'green': 0.10388148148148148, 'red': 0.12741925925925926}


if __name__ == '__main__':
    unittest.main()

