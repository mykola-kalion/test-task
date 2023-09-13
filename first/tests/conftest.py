from playwright.sync_api import sync_playwright
import pytest

from first.config import get_url
from first.src.pages.pages_urls import WikiPages


@pytest.fixture(scope='session')
def context():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope='session')
def sites_to_programming_languages_page(context):
    page = context.new_page()
    url = get_url(WikiPages.SITES_TO_PROGRAMMING_LANGUAGES)
    page.goto(url)
    yield page
    page.close()
