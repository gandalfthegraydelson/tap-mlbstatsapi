"""Stream type classes for tap-mlbstatsapi."""

from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_mlbstatsapi.client import MLBStatsAPIStream

import statsapi

from time import sleep


class ScheduleStream(MLBStatsAPIStream):
    """Define custom stream."""

    name = "schedule"
    # primary_keys = ["id"]
    replication_key = "game_date"
    schema = th.PropertiesList(
        th.Property("game_id", th.IntegerType),
        th.Property("game_date", th.StringType),
        th.Property("game_datetime", th.StringType),
        th.Property("game_type", th.StringType),
        th.Property("status", th.StringType),
        th.Property("away_name", th.StringType),
        th.Property("home_name", th.StringType),
        th.Property("away_id", th.IntegerType),
        th.Property("home_id", th.IntegerType),
        th.Property("doubleheader", th.StringType),
        th.Property("game_num", th.IntegerType),
        th.Property("home_probable_pitcher", th.StringType),
        th.Property("away_probable_pitcher", th.StringType),
        th.Property("home_pitcher_note", th.StringType),
        th.Property("away_pitcher_note", th.StringType),
        th.Property("away_score", th.IntegerType),
        th.Property("home_score", th.IntegerType),
        th.Property("current_inning", th.IntegerType),
        th.Property("inning_state", th.StringType),
        th.Property("venue_id", th.IntegerType),
        th.Property("venue_name", th.StringType),
        th.Property("winning_team", th.StringType),
        th.Property("losing_team", th.StringType),
        th.Property("winning_pitcher", th.StringType),
        th.Property("losing_pitcher", th.StringType),
        th.Property("save_pitcher", th.StringType),
        th.Property("summary", th.StringType),
        ).to_dict()

    def get_records(self, context: Optional[dict]) -> Iterable[dict]:
        start_date_default = f"{self.season}-01-01"
        start_date = self.get_starting_replication_key_value(context) or start_date_default
        end_date = f"{self.season}-12-31"
        games = statsapi.schedule(start_date=start_date, end_date=end_date)
        for game in games:
            if game["status"] != "Scheduled":
                yield game