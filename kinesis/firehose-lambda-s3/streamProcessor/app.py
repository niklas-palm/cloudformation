import json
import base64
import boto3
# import requests

client = boto3.client('comprehend')


def process_record(data):
    """
    Second return argument status = Ok | Dropped | ProcessingFailed
    For info: https://docs.aws.amazon.com/kinesisanalytics/latest/dev/lambda-preprocessing.html

    """

    def getDominantLanguage(text):
        res = client.detect_dominant_language(
            Text=text
        )

        res = res['Languages']

        if len(res) < 2:
            return res[0]['LanguageCode']  # Return only identified language
        else:
            scores = [x['Score'] for x in res]
            index = scores.index(max(scores))
            return res[index]['LanguageCode']

    def getSentiment(text, language_code='en'):

        sent_response = client.detect_sentiment(
            Text=text,
            LanguageCode=language_code
        )

        return sent_response

    dominant_language = getDominantLanguage(data['Tweet'])

    if not dominant_language == 'en':
        return {}, 'Dropped'

    sentiment_res = getSentiment(data['Tweet'])
    data['SENTIMENT'] = sentiment_res['Sentiment']
    # Process data

    return data, 'Ok'


def decodeData(data):
    byte_string = base64.b64decode(data)
    decoded = byte_string.decode('utf-8')
    return json.loads(decoded)


def encodeData(data):
    stringified = json.dumps(data)
    stringified = stringified + '\n'
    encoded = stringified.encode('utf-8')
    b64 = base64.b64encode(encoded)
    return b64.decode('utf-8')

# Main handler


def lambda_handler(event, context):

    processed_records = []

    print('START --------  \n')
    print('\n')
    print('Processing {} records'.format(len(event['records'])))
    print('\n')

    for record in event['records']:

        decoded = decodeData(record['data'])
        new_record, status = process_record(decoded)

        # if status != 'Ok':

        #     print('\n')
        #     print('decoded, before processing:')
        #     print(decoded)

        #     print('\n')
        #     print('status: ')
        #     print(status)

        #     print('\n')
        #     print('new_record: ')
        #     print(new_record)

        processed_records.append({
            "recordId": record['recordId'],
            "result": status,
            "data": encodeData(new_record)
        })

    return {"records": processed_records}

    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        # api-gateway-simple-proxy-for-lambda-input-format
        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
