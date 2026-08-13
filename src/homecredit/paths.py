"""Project paths that work on Kaggle without downloading data locally."""

from __future__ import annotations

import os
from pathlib import Path

KAGGLE_DATA_ROOT = Path("/kaggle/input/home-credit-credit-risk-model-stability")


def get_data_root(*, must_exist: bool = True) -> Path:
    """Return the Home Credit data directory.

    Set ``HOME_CREDIT_DATA_ROOT`` to override the Kaggle location when using a
    small local fixture. The full dataset should never be copied into this repo.
    """

    path = Path(os.environ.get("HOME_CREDIT_DATA_ROOT", KAGGLE_DATA_ROOT))
    if must_exist and not path.exists():
        raise FileNotFoundError(
            f"Home Credit data not found at {path}. "
            "Attach the competition dataset in Kaggle or set "
            "HOME_CREDIT_DATA_ROOT to a small local fixture."
        )
    return path

