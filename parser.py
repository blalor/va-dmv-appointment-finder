# -*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
import dateutil.parser


def parse_doc(body):
    soup = BeautifulSoup(body, "html.parser")

    available_dates = []
    for elt in soup.find_all(class_="activeday"):
        available_dates.append(dateutil.parser.parse(elt["day"]))

    return available_dates
