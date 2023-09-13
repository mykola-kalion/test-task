from playwright.sync_api import Page

from first.src.elements.content import Content
from first.src.elements.sites_to_laguages_table import SitesToLanguagesTable


class Article:
    def __init__(self, page: Page):
        self.table = SitesToLanguagesTable(page)
        self.content = Content(page)

    def get_table_data(self):
        return self.table.get_table_data()

    def get_some_content(self):
        return self.content.get_content()
