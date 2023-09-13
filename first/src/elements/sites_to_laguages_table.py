from playwright.sync_api import Page

from first.src.elements.table import Table
from first.src.helpers import table_header_to_keys, parse_popularity, remove_annotations
from first.src.models.sites_to_languages_popularity import SitesToLanguagesPopularity


class SitesToLanguagesTable(Table):
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
        return SitesToLanguagesPopularity(**data)

    def get_table_data(self):
        return self.combine_header_and_rows(self.get_header(), self.get_rows())
