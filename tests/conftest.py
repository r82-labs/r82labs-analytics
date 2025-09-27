import polars as pl
import pytest
from datetime import date


@pytest.fixture
def df():
    return pl.DataFrame(
        {
            "a": [1, None, 3, None],
            "b": ["x", "y", None, "y"],
            "c": [True, None, False, False],
            "d": [date(2020, 1, 1), None, date(2020, 1, 3), date(2020, 1, 4)],
        }
    )


@pytest.fixture
def df_expected():
    return pl.DataFrame(
        {
            "a": [1, 2, 3, 2],
            "b": ["x", "y", "y", "y"],
            "c": [True, False, False, False],
            "d": [
                date(2020, 1, 1),
                date(2020, 1, 4),
                date(2020, 1, 3),
                date(2020, 1, 4),
            ],
        }
    )
