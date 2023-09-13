import pytest
from playwright.sync_api import Page

from first.src.pages.article import ArticleTable


@pytest.fixture(scope='session')
def table_sites_popularity(page: Page):
    table = ArticleTable(page)
    data = table.get_table_data()
    yield data
