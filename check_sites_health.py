import requests
import argparse
import whois
from colorama import init, Fore


def load_urls4check(filepath):
    with open(filepath, "r") as text_file:
        return text_file.read()


def is_server_respond_with_200(url):
    response = requests.get(url)
    return response.status_code


def get_domain_expiration_date(url):
    return whois.whois(url).expiration_date


def print_the_result(url, status_code, expiration_date):
    print('\nUrl: {}\nStatus code: {}\nExpiration date: {}'.format(
        url, status_code, expiration_date))


def print_the_error(url):
    init()
    print('\nUrl: {}\n{}Seems like dns lookup failed.{}'.format(
        url, Fore.RED, Fore.RESET))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filepath',
        help='The path to the image')
    arguments = parser.parse_args()
    url_list = load_urls4check(arguments.filepath).split('\n')
    for url in url_list:
        try:
            status_code = is_server_respond_with_200(url)
            expiration_date = get_domain_expiration_date(url)
            print_the_result(url, status_code, expiration_date)
        except requests.exceptions.ConnectionError:
            print_the_error(url)
