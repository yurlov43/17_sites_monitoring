import requests
import argparse
import whois
from datetime import datetime


def load_urls4check(filepath):
    with open(filepath, "r") as text_file:
        return text_file.read()


def check_is_server_respond_with_200(url):
    response = requests.get(url)
    status_code = response.status_code
    if status_code != 200:
        return 'Something went wrong.'
    return 'Good! Status code: 200'


def check_domain_expiration_date(url):
    expiration_date = whois.whois(url).expiration_date
    if type(expiration_date) is list:
        expiration_date = expiration_date[0]
    number_of_days = (expiration_date - today).days
    if number_of_days <= 30:
        return 'Less than a month left before the expiration date.'
    return 'Good! Until the expiry date is more than a month.'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filepath',
        help='The path to the image')
    arguments = parser.parse_args()
    url_list = load_urls4check(arguments.filepath).split('\n')
    today = datetime.now()
    for url in url_list:
        print('\nURL: {}'.format(url))
        try:
            print(check_is_server_respond_with_200(url))
            print(check_domain_expiration_date(url))
        except requests.exceptions.ConnectionError:
            print('Seems like dns lookup failed.')
