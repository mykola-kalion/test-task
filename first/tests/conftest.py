from playwright.sync_api import sync_playwright, Page
import pytest

from first.src.pages.article import ArticleTable


@pytest.fixture(scope='session')
def context():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope='session')
def page(context):
    page = context.new_page()
    page.goto("https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites")
    yield page
    page.close()
