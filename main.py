import scraper.scraper_requests as scraper_requests
import utilities.scraper_utils as utils
import utilities.strings as strings
import argparse
import os
import glob


def parse_arguments():
    parser = argparse.ArgumentParser(description='Get TV Shows transcripts.')
    parser.add_argument('show_name',
                        metavar='Show name',
                        help='The name of the show.')
    parser.add_argument("--clean",
                        help="clean output files.",
                        action="store_true")
    return parser.parse_args()


def get_episode_transcript(show_name, season, episode):
    file_name = strings.file_format.format(show_name, season, episode)
    scraper_requests.get_script_for_episode_of_show(
        show_name, season, episode, file_name)


def clean(show_name):
    for f in glob.glob("output/{0}*".format(show_name)):
        os.remove(f)


def main():
    args = parse_arguments()

    show_name = utils.parse_show_name(args.show_name)
    if args.clean:
        prompt = input(strings.clean_message.format(show_name))
        if prompt.upper() == 'Y':
            clean(show_name)
        exit()

    try:
        num_of_seasons = scraper_requests.get_number_of_seasons_for_show(
            show_name)
        season = int(
            input(strings.season_prompt_message.format(num_of_seasons)))
        if season in range(1, num_of_seasons + 1):
            num_of_episodes = scraper_requests.get_number_of_episodes_for_season_of_show(
                show_name, season)
            episode = int(
                input(strings.episode_prompt_message.format(num_of_episodes)))
            if episode in range(1, num_of_episodes + 1):
                get_episode_transcript(show_name, season, episode)
    except Exception as ex:
        print(ex)
        exit()


if __name__ == "__main__":
    main()
