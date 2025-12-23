from __future__ import annotations
import pandas as pd

def safe_left_join(
    left: pd.DataFrame,
    right: pd.DataFrame,
    on: str | list[str],
    *,
    validate: str,
    suffixes: tuple[str, str] = ("", "_r"),
) -> pd.DataFrame:
    # --- ensure join keys have same dtype ---
    keys = [on] if isinstance(on, str) else on

    for k in keys:
        left[k] = left[k].astype("string")
        right[k] = right[k].astype("string")

    return left.merge(
        right,
        how="left",
        on=on,
        validate=validate,
        suffixes=suffixes,
    )
