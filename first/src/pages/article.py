from playwright.sync_api import Page

from first.src.helpers import table_header_to_keys, parse_popularity, remove_annotations
from first.src.models.sites_to_languages_popularity import SitesToLanguagesPopularityStatistics


class Table:
    table_locator = lambda _, name: f"//caption[normalize-space(text()) = '{name}']/ancestor::table"

    def __init__(self, page: Page, table_name: str):
        self.page = page
        self.table = self.page.wait_for_selector(self.table_locator(table_name))

    def _get_header(self) -> list[str]:
        return [el.inner_text() for el in self.table.query_selector_all("//thead//th")]

    def _get_rows(self) -> list[list[str]]:
        rows = self.table.query_selector_all("//tbody//tr")
        rows_data = []

        for row in rows:
            cells_data = [cell.inner_text() for cell in row.query_selector_all("//child::td")]
            rows_data.append(cells_data)

        return rows_data

    def _combine_result(self, header, rows):
        return [dict(zip(header, row)) for row in rows]


class ArticleTable(Table):
    def __init__(self, page: Page):
        super().__init__(page, table_name="Programming languages used in most popular websites*")

    def get_header(self) -> list[str]:
        els = self._get_header()
        return list(map(table_header_to_keys, els))

    def get_rows(self) -> list[list[str]]:
        els = self._get_rows()
        data = []
        for row in els:
            data.append([remove_annotations(cell) for cell in row])
        return data

    def combine_header_and_rows(self, header: list[str], rows: list[list[str]]):
        combined = [dict(zip(header, row)) for row in rows]
        return [self.convert_data_to_dataclass(element) for element in combined]

    def convert_data_to_dataclass(self, data: dict):
        data["popularity"] = parse_popularity(data["popularity"])
        data["back_end"] = data["back_end"].split(",")
        data["front_end"] = data["front_end"].split(",")
        data["database"] = data["database"].split(",")
        return SitesToLanguagesPopularityStatistics(**data)

    def get_table_data(self):
        return self.combine_header_and_rows(self.get_header(), self.get_rows())
