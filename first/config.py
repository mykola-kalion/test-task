import os
import urllib.parse

baseUrlFromEnv = os.getenv('BASE_URL')

baseUrl = baseUrlFromEnv if baseUrlFromEnv else "https://en.wikipedia.org"


def get_url(url: str):
    return urllib.parse.urljoin(baseUrl, url)
