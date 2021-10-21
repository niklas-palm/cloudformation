import time
import json

time.sleep(1)


def lambda_handler(event, context):
    time.sleep(0.2)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message ": "ok"
        })
    }
