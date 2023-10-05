import requests
from dataclasses import dataclass
from typing import List


@dataclass
class DepartureInfo:
    delay: int
    planned_departure: int
    platform: str
    vehicle_type: str
    terminus: str
    
    @classmethod
    def from_api_object(cls, object: dict):
        return cls(
            delay=int(object["delay"]),
            planned_departure=int(object["time"]),
            platform=object["platform"],
            terminus=object["station"],
            vehicle_type=object["vehicleinfo"]["type"]
        )


@dataclass
class LiveBoard:
    station: str
    last_update: int #epoch time
    departures: List[DepartureInfo]

    @classmethod
    def from_api_object(cls, object: dict):
        return cls(
            station=object["station"],
            last_update= int(object["timestamp"]),
            departures = [DepartureInfo.from_api_object(departure) for departure in object["departures"]["departure"]]
        )



def live_board(station: str) -> dict:
    """Fetch the live board for a given station."""
    url = f"https://api.irail.be/liveboard/?station={station}&format=json"
    object = requests.get(url).json()
    return LiveBoard.from_api_object(object)