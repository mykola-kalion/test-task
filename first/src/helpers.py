import re


def table_header_to_keys(key: str):
    fields_mapping = {
        "Websites": "website",
        "Popularity": "popularity",
        "Front-end": "front_end",
        "Back-end": "back_end",
        "Database": "database",
        "Notes": "notes"
    }

    return fields_mapping[key.split("\n")[0]]


def parse_popularity(text):
    number_from_string = re.match(r'\d+(?:(,|.)\d+)+', text).group()
    without_delimiter = number_from_string.replace(",", "").replace(".", "")

    return int(without_delimiter)


def remove_annotations(cell_data: str):
    return re.sub(r"\[\d+]", "", cell_data)
