"""
Scrape web data for url, phone and emails.
"""


__author__ = 'Haley Collard'


import requests
import argparse
import sys
import re


def create_parser():
    parser = argparse.ArgumentParser(
        description="Scrape web for data.")
    parser.add_argument('url', help='website to scrape')
    return parser


def main(args):
    parser = create_parser()
    ns = parser.parse_args()
    url = ns.url
    html = requests.get(url).text
    url_pattern = r'href=("(https?:\/\/)?(www\.)?\w+\.\S+)"'
    email_pattern = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    phone_pattern = r'[(\d]?\d{3}[-.()]?\d{3}[-.]?\d{4}'
    urls = re.findall(url_pattern, html)
    emails = re.findall(email_pattern, html)
    phone_nums = re.findall(phone_pattern, html)
    print('URLS:')
    for url in urls:
        print(url[0])
    print('EMAILS:')
    for email in emails:
        print(email)
    print('PHONE NUMBERS:')
    for phone_num in phone_nums:
        print(phone_num)


if __name__ == '__main__':
    main(sys.argv[1:])
