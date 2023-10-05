from src.fetch_data import LiveBoard, DepartureInfo
from datetime import datetime
from math import floor

#function to convert epoch time to human readable time
def epoch_to_human(epoch_time: int) -> str:
    """converts epoch time to human readable time"""
    return datetime.fromtimestamp(epoch_time).strftime('%H:%M:%S')

def live_board_view(live_board: LiveBoard) -> str:
    """creates an html view of the live board"""
    view = f"""
    <html>
        <head>
            <title>Live board for {live_board.station}</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
        </head>
        <body>
            <h1>Live board for {live_board.station}</h1>
            <p>Last update: {epoch_to_human(live_board.last_update)}</p>
            <table>
                <tr>
                    <th>Departure time</th>
                    <th>Delay (Minutes)</th>
                    <th>Departs in (Minutes)</th>
                    <th>Platform</th>
                    <th>Vehicle type</th>
                    <th>Terminus</th>
                </tr>
    """
    for departure in live_board.departures:
        view += f"""
                <tr>
                    <td>{epoch_to_human(departure.planned_departure)}</td>
                    <td>{(departure.delay/60)}</td>
                    <td>{floor((departure.planned_departure - live_board.last_update)/60 + (departure.delay/60))}</td>
                    <td>{departure.platform}</td>
                    <td>{departure.vehicle_type}</td>
                    <td>{departure.terminus}</td>
                </tr>
        """
    view += """
            </table>
        </body>
    </html>
    """
    return view