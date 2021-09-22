from typing import Iterable
from bs4 import BeautifulSoup
from requests import get
from re import compile, Pattern


def remtags(s: str, p: Pattern = compile(r"<.*?>")) -> str:
    """remove HTML tags in a string."""
    r = p.search(s)
    if not r:
        return s
    else:
        return remtags(s[: r.start()] + s[r.end() :], p)


def remtags_in_list(l: list[str], p: Pattern = compile(r"<.*?>")) -> list:
    """remove HTML tags in strings in a list."""
    r = []
    for i in l:
        r.append(remtags(i, p))
    return r


def soupfy(url: str) -> BeautifulSoup:
    """return an instance of BeautifulSoap from the url given."""
    return BeautifulSoup(get(url).content, "html.parser")


def search_results(target_string: str, target_iterable: Iterable[str]) -> list:
    """return a list of strings that contain target_string, from
    target_iterable of str's."""
    result = list()
    p = compile(target_string)
    for i in target_iterable:
        if p.search(i):
            result.append(i)
    return result
