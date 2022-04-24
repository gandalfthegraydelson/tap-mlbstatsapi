"""MLBStatsAPI tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_mlbstatsapi.streams import ScheduleStream

STREAM_TYPES = [ScheduleStream]


class TapMLBStatsAPI(Tap):
    """MLBStatsAPI tap class."""

    name = "tap-mlbstatsapi"

    config_jsonschema = th.PropertiesList(th.Property("season", th.IntegerType, default=2022)).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
