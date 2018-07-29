base_url = "https://www.springfieldspringfield.co.uk/"
show_query_format = "tv-show={0}"
season_query_format = "season={0}"
episode_query_format = "episode=s{0:02d}e{1:02d}"


def parse_show_name(show_name):
    return show_name.lower().replace(' ', '-')


def get_show_base_url_formatted(view=False):
    result = base_url
    if view:
        result += "view_"
    result += "episode_scripts.php" + "?" + show_query_format
    return result


def get_show_url(show, view=False):
    show_name_parsed = parse_show_name(show)
    return get_show_base_url_formatted(view).format(show_name_parsed)


def get_season_url(show, season):
    return get_show_url(show) + "&" + season_query_format.format(season)


def get_episode_url(show, season, episode):
    episode_url = get_show_url(show, True) + "&" + episode_query_format
    return episode_url.format(season, episode)
