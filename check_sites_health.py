import requests
import argparse
import whois
from datetime import datetime


def load_text(filepath):
    with open(filepath, 'r') as text_file:
        return text_file.read()


def get_server_response_with_ok(url):
    response = requests.get(url)
    return response.ok


def get_domain_expiration_date(url):
    expiration_date = whois.whois(url).expiration_date
    if type(expiration_date) is list:
        expiration_date = expiration_date[0]
    return expiration_date


def calculate_reserve_days(expiration_date):
    if expiration_date:
        reserve_days = (expiration_date - today).days
    else:
        return None
    return reserve_days


def print_messages_to_console(server_respond_ok, reserve_days, number_of_days):
    if server_respond_ok:
        print('Good! The server is OK.')
    else:
        print('Something went wrong.')
    if reserve_days and reserve_days <= number_of_days:
        print('Less than a month left before the expiration date.')
    else:
        print('Good! Until the expiry date is more than a month.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filepath',
        help='The path to the image')
    arguments = parser.parse_args()
    url_list = load_text(arguments.filepath).split('\n')
    today = datetime.now()
    number_of_days = 30
    for url in url_list:
        print('\nURL: {}'.format(url))
        try:
            server_respond_ok = get_server_response_with_ok(url)
            expiration_date = get_domain_expiration_date(url)
            reserve_days = calculate_reserve_days(expiration_date)
            print_messages_to_console(
                server_respond_ok,
                reserve_days,
                number_of_days)
        except requests.exceptions.ConnectionError:
            print('Seems like dns lookup failed.')
