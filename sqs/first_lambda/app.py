import os
import boto3
import json
# Download Stuff from S3 and initialise a model here, outside of handler.

NEXT_QUEUE_URL = os.environ["FIRST_INTERNAL_QUEUE_URL"]
client = boto3.client('sqs')


def lambda_handler(event, context):
    print('First lambda')
    print('processesing {} records'.format(len(event['Records'])))

    payloads = []

    for record in event['Records']:
        print(record['body'])
        payload = {}

        payload['ApproximateFirstLambdaReceiveTimestamp'] = record['attributes']['ApproximateFirstReceiveTimestamp']

        # This just passes along original body - not necessary
        payload['OriginalBody'] = record['body']
        payload['ProcessedBody'] = doStuff(record['body'])
        payloads.append(payload)

    response = client.send_message(
        QueueUrl=NEXT_QUEUE_URL,
        MessageBody=json.dumps({'Payloads': payloads})
    )

    if not response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print('---- ERROR when writing to queue: \n')
        print(response)
        raise Exception(
            'Something went wrong when writing processed records to the queue', response)

    return


def doStuff(payload):
    return 'NEW INFO FROM PROCESSING GOES HERE'
