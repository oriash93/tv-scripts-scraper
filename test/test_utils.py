import unittest
import utils.scraper_utils as utils


class ScraperUtilsTests(unittest.TestCase):
    def test_parse_show_name_with_space(self):
        expected = "the-blacklist"
        value = utils.parse_show_name("The Blacklist")
        self.assertEqual(value, expected)

    def test_parse_show_name_all_caps(self):
        expected = "the-simpsons"
        value = utils.parse_show_name("THE SIMPSONS")
        self.assertEqual(value, expected)

    def test_parse_show_name_mixed(self):
        expected = "family-guy"
        value = utils.parse_show_name("fAmIly GuY")
        self.assertEqual(value, expected)

    def test_get_show_base_url_formatted_with_view(self):
        expected = "https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show={0}"
        value = utils.get_show_base_url_formatted(True)
        self.assertEqual(value, expected)

    def test_get_show_base_url_formatted_without_view(self):
        expected = "https://www.springfieldspringfield.co.uk/episode_scripts.php?tv-show={0}"
        value = utils.get_show_base_url_formatted()
        self.assertEqual(value, expected)

    def test_get_show_url(self):
        expected = "https://www.springfieldspringfield.co.uk/episode_scripts.php?tv-show=house-of-cards"
        value = utils.get_show_url('House of Cards')
        self.assertEqual(value, expected)

    def test_get_season_url_one_word(self):
        expected = "https://www.springfieldspringfield.co.uk/episode_scripts.php?tv-show=scorpion&season=3"
        value = utils.get_season_url('Scorpion', 3)
        self.assertEqual(value, expected)

    def test_get_season_url_multiple_words(self):
        expected = "https://www.springfieldspringfield.co.uk/episode_scripts.php?tv-show=king-of-the-hill&season=1"
        value = utils.get_season_url('King of the Hill', 1)
        self.assertEqual(value, expected)

    def test_get_episode_url_one_word(self):
        expected = "https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=supernatural&episode=s12e01"
        value = utils.get_episode_url('Supernatural', 12, 1)
        self.assertEqual(value, expected)

    def test_get_episode_url_multiple_words(self):
        expected = "https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=everybody-loves-raymond&episode=s01e22"
        value = utils.get_episode_url('Everybody Loves Raymond', 1, 22)
        self.assertEqual(value, expected)
