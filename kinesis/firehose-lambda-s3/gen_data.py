import boto3
import random
import time
import json
from datetime import date

client = boto3.client('firehose')


class tweet_generator():
    def __init__(self, tweets, authors):
        self.tweets = tweets
        self.authors = authors

    def gen_payload(self):
        today = date.today()

        d = today.strftime("%d/%m/%Y")
        return {"date": d, "Author": random.choice(self.authors), "Tweet": random.choice(self.tweets), }


if __name__ == "__main__":
    tweets = ['Hello, you are fine!', 'Amazing job today', 'Du är helt ok!', 'Idag fick vi betalt :D',
              'Yo no quiero trabajar más!', 'You asshole!', 'That wasnt very well done.']
    authors = ['Niklas', 'RandomGuy_90', 'Olechka', 'Jeff B', 'Nader']

    gen = tweet_generator(tweets, authors)

    # response = client.list_delivery_streams(
    #     # DeliveryStreamType='DirectPut'
    # )
    # print(response)

    i = 0
    while True:
        i += 1
        time.sleep(0.3)
        data = gen.gen_payload()
        if i % 10 == 0:
            print(data)
        res = client.put_record(
            DeliveryStreamName='fh-lambda-s3-deliveryStream-12Z6O0HVWW5GV',
            Record={'Data': bytes(json.dumps(data) + '\n', 'utf-8')}
        )
