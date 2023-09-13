import pytest
from playwright.sync_api import Page

from first.src.pages.article import Article

# There is no reason to make separate conftest. This was done as example.
@pytest.fixture(scope='session')
def table_sites_popularity(sites_to_programming_languages_page: Page):
    table = Article(sites_to_programming_languages_page)
    data = table.get_table_data()
    yield data
