import json
import time
import base64
import datetime

# import requests


def lambda_handler(event, context):
    print('Lambda was invoked')

    def base64ToString(str):
        return base64.b64decode(str).decode('utf-8')

    for key in event['records']:
        record = event['records'][key][0]
        print('RECORD: {}'.format(record))
        print('Topic: {}'.format(record['topic']))
        print('Partition: {}'.format(record['partition']))
        print('CREATED AT: {}'.format(
            datetime.datetime.fromtimestamp(record['timestamp']/1000.0)))
        print('DECODED MESSAGE: {}'.format(base64ToString(record['value'])))

    return
