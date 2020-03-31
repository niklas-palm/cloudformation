import os
import boto3
import json
# Download Stuff from S3 and initialise a model here, outside of handler.

NEXT_QUEUE_URL = os.environ["FIRST_INTERNAL_QUEUE_URL"]
client = boto3.client('sqs')


def lambda_handler(event, context):
    print('First lambda')
    print(event)
    print('\n')

    payloads = []

    for record in event['Records']:
        print(record)
        print(record['body'])
        payload = {}

        payload['ApproximateFirstLambdaReceiveTimestamp'] = record['attributes']['ApproximateFirstReceiveTimestamp']
        payload['body'] = record['body']
        payload['processed'] = doStuff(record['body'])
        payloads.append(payload)

    print(payloads)
    print('\n')

    response = client.send_message(
        QueueUrl=NEXT_QUEUE_URL,
        MessageBody=json.dumps({'Payloads': payloads})
    )

    print(response)

    return


def doStuff(payload):
    return 'NEW INFO FROM PROCESSING GOES HERE'
