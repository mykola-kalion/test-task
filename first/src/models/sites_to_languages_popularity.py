import dataclasses


@dataclasses.dataclass
class SitesToLanguagesPopularityStatistics:
    website: str
    popularity: int
    front_end: list[str]
    back_end: list[str]
    database: list[str]
    notes: str
