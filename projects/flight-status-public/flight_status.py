#!/usr/bin/env python3
"""Print a flight status from a bundled timetable."""

from __future__ import annotations

import json
import sys
from pathlib import Path

TIMETABLE_PATH = Path(__file__).with_name("timetable.json")


def load_timetable() -> dict[str, dict[str, str]]:
    with TIMETABLE_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def status_for(flight_code: str) -> str:
    timetable = load_timetable()
    flight = timetable.get(flight_code.upper())
    if flight is None:
        return f"Flight {flight_code.upper()}: unknown flight code"
    return f"Flight {flight_code.upper()}: {flight['status']}"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python flight_status.py <flight-code>")
        return 1

    print(status_for(sys.argv[1]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
