import boto3
import logging
import random

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

# apply the XRay handler to all clients.
patch_all()

client = boto3.client('events')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    events = [
        {
            "Source": "com.mycompany.myapp",
            "DetailType": "OrderCreated",
            "Detail": "{\"OrderValue\": 1000}, \"OtherInfo\": \"Wow\"}",
            "EventBusName": "my-custom-event-bus"
        },
        {
            "Source": "com.mycompany.myapp",
            "DetailType": "OrderCreated",
            "Detail": "{\"OrderValue\": 100}, \"OtherInfo\": \"hey\"}",
            "EventBusName": "my-custom-event-bus"
        },
        {
            "Source": "com.mycompany.myapp",
            "DetailType": "OrderCreated",
            "Detail": "{\"OrderValue\": 10}, \"OtherInfo\": \"heyyou\"}",
            "EventBusName": "my-custom-event-bus"
        },
        {
            "Source": "com.mycompany.myapp",
            "DetailType": "OrderCreated",
            "Detail": "{\"OrderValue\": 100000, \"OtherInfo\": \"Wow\"}",
            "EventBusName": "my-custom-event-bus"
        },
        {
            "Source": "com.mycompany.myapp",
            "DetailType": "OrderCanceled",
            "Detail": "{\"OrderValue\": 100000, \"OtherInfo\": \"Cancelled orde because why not\"}",
            "EventBusName": "my-custom-event-bus"
        }
    ]

    logger.info('### Putting events')

    response = client.put_events(
        Entries=[random.choice(events)]
    )

    logger.info('### Response')
    logger.info(response)

    return
