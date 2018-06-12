import requests
import argparse
import whois
from colorama import init, Fore
from datetime import datetime


def load_urls4check(filepath):
    with open(filepath, "r") as text_file:
        return text_file.read()


def is_server_respond_with_200(url):
    response = requests.get(url)
    return response.status_code


def get_domain_expiration_date(url):
    return whois.whois(url).expiration_date


def print_the_result(status_code, expiration_date):
    print('Status code: {}\nExpiration date: {}'.format(
        status_code, expiration_date))


def print_the_error(error):
    init()
    print('{}{}{}'.format(Fore.RED, error, Fore.RESET))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filepath',
        help='The path to the image')
    arguments = parser.parse_args()
    url_list = load_urls4check(arguments.filepath).split('\n')
    today = datetime.now()
    for url in url_list:
        print('\n{}'.format(url))
        try:
            status_code = is_server_respond_with_200(url)
            if status_code != 200:
                print_the_error('Something went wrong.')
            expiration_date = get_domain_expiration_date(url)
            if type(expiration_date) is list:
                expiration_date = expiration_date[0]
            number_of_days = (expiration_date - today).days
            if number_of_days <= 30:
                print_the_error(
                    'Less than a month left before the expiration date.')
            print_the_result(status_code, expiration_date)
        except requests.exceptions.ConnectionError:
            print_the_error('Seems like dns lookup failed.')
