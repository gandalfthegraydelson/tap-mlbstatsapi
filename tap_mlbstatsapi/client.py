"""REST client handling, including MLBStatsAPIStream base class."""

import requests
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import Tap, Stream

from memoization import cached

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class MLBStatsAPIStream(Stream):
    """MLBStatsAPI stream class."""

    def __init__(self, tap: Tap):
        super().__init__(tap)
        self.season = self.config.get("season")
