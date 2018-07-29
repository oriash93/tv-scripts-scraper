import unittest
import scraper.scraper_requests as scraper_requests


class ScraperRequestsTests(unittest.TestCase):
    def test_get_number_of_seasons_for_show(self):
        expected = 2
        value = scraper_requests.get_number_of_seasons_for_show(
            'Designated Survivor 2016')
        self.assertEqual(value, expected)

    def test_get_number_of_episodes_for_season_of_show(self):
        expected = 10
        value = scraper_requests.get_number_of_episodes_for_season_of_show(
            'Narcos 2015', 1)
        self.assertEqual(value, expected)

    def test_get_total_number_of_episodes_for_show(self):
        expected = 62
        value = scraper_requests.get_total_number_of_episodes(
            'Breaking Bad')
        self.assertEqual(value, expected)
