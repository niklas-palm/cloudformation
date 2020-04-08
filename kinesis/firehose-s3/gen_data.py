import boto3
import random
import time
import json

from datetime import datetime

client = boto3.client('firehose')


class data_generator():
    def __init__(self, sectors):
        self.payload = {}

        for sector in sectors:
            self.payload[sector] = random.randint(20, 50)

    def get(self):
        print(self.payload)

    def gen_payload(self):

        for sector in self.payload:
            self.payload[sector] = round(
                self.payload[sector] + random.uniform(-3, 3), 2)

        return self.payload


if __name__ == "__main__":
    sectors = ['HEALTH_CARE', 'TECH', 'AUTOMMOBILE', 'RETAIL']
    gen = data_generator(sectors)

    # for i in range(10):
    i = 0
    while True:
        i += 1
        time.sleep(60)
        data = gen.gen_payload()
        now = datetime.now()
        date = {'date': now.strftime("%d/%m/%Y %H:%M:%S")}
        temp = data.copy()
        temp.update(date)

        if i % 5 == 0:
            print(temp)
        res = client.put_record(
            DeliveryStreamName='firehouse-s3-deliveryStream-U8V0OCL7WIBD',
            Record={'Data': bytes(json.dumps(temp) + '\n', 'utf-8')}
        )
