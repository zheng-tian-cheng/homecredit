import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from homecredit.paths import get_data_root


class DataRootTest(unittest.TestCase):
    def test_environment_override(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with patch.dict(os.environ, {"HOME_CREDIT_DATA_ROOT": directory}):
                self.assertEqual(get_data_root(), Path(directory))

    def test_missing_path_has_actionable_error(self) -> None:
        with patch.dict(
            os.environ,
            {"HOME_CREDIT_DATA_ROOT": "/definitely/missing/home-credit-data"},
        ):
            with self.assertRaisesRegex(FileNotFoundError, "Attach the competition"):
                get_data_root()


if __name__ == "__main__":
    unittest.main()

