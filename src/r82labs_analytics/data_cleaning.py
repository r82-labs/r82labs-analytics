import polars as pl
import polars.selectors as cs


def default_empty_cells(df: pl.DataFrame) -> pl.DataFrame:
    df_filled = df.with_columns(
        cs.numeric().fill_null(cs.numeric().mean()),
        cs.boolean().fill_null(cs.boolean().mode().first()),
        cs.string().fill_null(cs.string().mode().first()),
        cs.date().fill_null(cs.date().max()),
    )

    return df_filled
