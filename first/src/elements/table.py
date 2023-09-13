from playwright.sync_api import Page


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
