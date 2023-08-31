from typing import Optional

def lambda_handler(event: dict, context: Optional[dict] = None):
    print("Hello world")
    return {"statusCode": 200, "body": "Goodbye world"}