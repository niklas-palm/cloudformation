## DynamoDB Streams Lambda trigger

This cloudformation template illustrates how AWS SAM can be used to set up a Lambda function that is triggered by a DynamoDB Stream. After deploying this template,

```bash
aws dynamodb put-item --item '{"id": {"S": "123"}, "payload": {"S": "This is message"}}' --table-name <table-name>
```

will post an object to the table, triggering the Lambda function.
