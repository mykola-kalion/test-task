import pytest
from assertpy import assert_that, soft_assertions


@pytest.mark.parametrize("expected_popularity", [
    10 ** 7,
    1.5 * (10 ** 7),
    5 * (10 * 7),
    10 ** 8,
    5 * (10 ** 8),
    10 ** 9,
    1.5 * (10 * 9)
])
@pytest.mark.wiki
@pytest.mark.first
def test_sites_popularity(table_sites_popularity, expected_popularity):
    with soft_assertions():
        for element in table_sites_popularity:
            error = f"{element.website} (Frontend:{''.join(element.front_end)} | Backend:{','.join(element.back_end)}"
            assert_that(element.popularity).described_as(error).is_greater_than_or_equal_to(expected_popularity)
