import utils.scraper_utils as utils
import requests
import sys
from bs4 import BeautifulSoup


def get_number_of_seasons_for_show(show):
    r = requests.get(utils.get_show_url(show))
    soup = BeautifulSoup(r.text, "lxml")
    return len(soup.select('div.script-season-links > a'))


def get_episodes_for_season_of_show(show, season):
    r = requests.get(utils.get_season_url(show, season))
    soup = BeautifulSoup(r.text, "lxml")
    return [link.href for link in soup.select('a.season-episode-title')]


def get_number_of_episodes_for_season_of_show(show, season):
    return len(get_episodes_for_season_of_show(show, season))


def get_total_number_of_episodes(show):
    episodes_total = 0
    for season in range(get_number_of_seasons_for_show(show)):
        episodes_total += get_number_of_episodes_for_season_of_show(
            show, season + 1)
    return episodes_total


def get_script_for_episode_of_show(show, season, episode, output=None):
    r = requests.get(utils.get_episode_url(show, season, episode))
    soup = BeautifulSoup(r.text, "lxml")
    script_section = soup.find("div", {"class": "scrolling-script-container"})
    script_text = script_section.text.strip()

    handle = open(output, 'w', encoding="utf-8") if output else sys.stdout
    try:
        handle.write(script_text)
    except Exception as identifier:
        print(identifier)
    finally:
        if handle is not sys.stdout:
            handle.close()
