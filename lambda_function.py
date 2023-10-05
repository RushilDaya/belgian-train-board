from typing import Optional
from src.fetch_data import live_board
from src.create_view import live_board_view
from src.update_webpage import update_webpage

STATION='Leuven'

def lambda_handler(event: dict, context: Optional[dict] = None):
    data = live_board(STATION)
    view = live_board_view(data)
    update_webpage(view)
    return {"statusCode": 200, "body": "Goodbye world"}

if __name__ == "__main__":
    lambda_handler({})