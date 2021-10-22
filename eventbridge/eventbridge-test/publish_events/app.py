import boto3
import logging
import random
import json
import os

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

# apply the XRay handler to all clients.
patch_all()

client = boto3.client('events')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def getDetailType():
    if random.randint(1, 100) < 5:
        return 'OrderCanceled'
    else:
        return 'OrderCreated'


def lambda_handler(event, context):
    events = []
    for i in range(10):

        event = {}
        event['EventBusName'] = os.environ['EVENT_BUS']
        event['Source'] = "com.mycompany.myapp"
        event['DetailType'] = getDetailType()

        OrderValue = {'OrderValue':  random.randint(1, 10000)}
        event['Detail'] = json.dumps(OrderValue)

        events.append(event)

    logger.info('### Putting events')

    response = client.put_events(
        Entries=events
    )

    logger.info('### Response')
    logger.info(response)

    return
