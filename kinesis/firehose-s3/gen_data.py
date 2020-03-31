import boto3
import random
import time
import json

client = boto3.client('firehose')


class data_generator():
    def __init__(self, sectors):
        self.payload = {}
        # self.sectors = sectors
        # self.prices =
        for sector in sectors:
            # self.payload['sector'] = sector
            # self.payload['price'] = random.randint(20, 50)
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

    # response = client.list_delivery_streams(
    #     # DeliveryStreamType='DirectPut'
    # )

    # response = client.describe_delivery_stream(
    #     DeliveryStreamName='test-firehose-deliveryStream-HYZBR513I76K'
    # )
    # print('\n')
    # print(response)
    # print('\n')

    for i in range(10):
        time.sleep(0.2)
        data = gen.gen_payload()
        if i % 5 == 0:
            print(data)
        res = client.put_record(
            DeliveryStreamName='test-firehose-deliveryStream-HYZBR513I76K',
            Record={'Data': bytes(json.dumps(data) + '\n', 'utf-8')}
        )
