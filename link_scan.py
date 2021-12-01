from typing import List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
import urllib
import sys


def get_links(url: str) -> list:
    """Find all links on page at the given url.
    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    driver.get(url)
    links = driver.find_elements_by_tag_name("a")
    actual_list = []
    for link in links:
        temp = link.get_attribute('href')
        if temp != None:
            if '#' in temp:
                temp = temp.split('#')[0]
            elif '?' in temp:
                temp = temp.split('?')[0]
            actual_list.append(temp)
    actual_list = list(dict.fromkeys(actual_list))
    return actual_list


def is_valid_url(url: str) -> bool:
    """Check if the url is valid and reachable.

    Returns:
        True if the URL is OK, False otherwise.
    """
    try:
        urllib.request.urlopen(url)
        return True
    except urllib.error.HTTPError:
        if urllib.error.HTTPError.code == 403:
            return True
        return False


def invalid_urls(urllist: List[str]) -> List[str]:
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    Returns:
        A new list containing only the invalid or unreachable URLs from the parameter list.
    """
    new_list = []
    for url in urllist:
        if is_valid_url == False:
            new_list.append(url)
    return new_list


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage:  python3 link_scan.py url\n\nTest all hyperlinks on the given url.")
        sys.exit(0)

    driver = webdriver.Chrome('/Users/premkul/Documents/isp/link-scanner/chromedriver')
    url = sys.argv[1]
    links = get_links(url)
    bad_links = invalid_urls(links)
    for url in links:
        print(url)

    print('\nBad Links:')
    for bad_link in bad_links:
        print(bad_link)
