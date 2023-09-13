import dataclasses


@dataclasses.dataclass
class SitesToLanguagesPopularity:
    website: str
    popularity: int
    front_end: list[str]
    back_end: list[str]
    database: list[str]
    notes: str
