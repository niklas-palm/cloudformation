import json

# import requests


def lambda_handler(event, context):
    print('DEAD_LETTER_QUEUE')
    print('The following record could not be processed correctly:')
    print(event)

    return
