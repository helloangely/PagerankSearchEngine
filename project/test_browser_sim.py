import browser_sim 
import unittest

class TestIndex(unittest.TestCase):
	def test_results_giver(self):
		eq = browser_sim.results_giver(["boy","longer","healing"])
		should_equal = [[0.041096885245210185, 'http://www.cnn.com/americas', 'Breaking News, Latest News and Videos - CNN.com'], [0.03601426809658935, 'http://www.cnn.com/africa', 'Africa News - CNN.com'], [0.03029646042331396, 'http://www.cnn.com/politics', 'CNNPolitics - Political News, Analysis and Opinion'], [0.02714615205992113, 'http://www.cnn.com/specials/us/crime-and-justice', 'Crime + Justice - CNN.com'], [0.025800821419386225, 'http://www.cnn.com/', 'CNN - Breaking News, Latest News and Videos'], [0.025800821419386225, 'http://www.cnn.com', 'CNN - Breaking News, Latest News and Videos'], [0.02410200547437113, 'http://www.cnn.com/style', 'CNN Style - Fashion, design, art, architecture and luxury - CNN.com'], [0.01921720650023496, 'http://www.cnn.com/videos', 'Video News - CNN.com'], [0.016190019813981934, 'http://www.cnn.com/specials/us/energy-and-environment', 'Energy + Environment - CNN.com'], [0.015569316178941094, 'http://www.cnn.com/specials/us/extreme-weather', 'Extreme Weather - CNN.com'], [0.01551681891789008, 'http://www.cnn.com/us', 'U.S. News - CNN.com'], [0.014704815804032738, 'http://www.cnn.com/entertainment', 'Entertainment News - Celebrities, Movies, TV, Music - CNN.com'], [0.013077748082393316, 'http://www.cnn.com/health', 'Health News - CNN.com'], [0.011202924538803621, 'http://www.cnn.com/world', 'World News - CNN.com'], [0.010236636277640166, 'http://www.cnn.com/travel', 'Travel News - CNN.com'], [0.0072880784469667795, 'http://www.cnn.com/opinions', 'Opinion, Commentary, Analysis - CNN.com'], [0.005196284685255031, 'http://bleacherreport.com', 'Bleacher Report | Sports. Highlights. News. Now.'], [0.0026679669826492666, 'http://www.cnn.com/specials/space-science', 'Space + Science - CNN.com']]
		self.assertEqual(eq,should_equal)

if __name__ == '__main__':
    unittest.main()