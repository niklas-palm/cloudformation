## Async processing with Lambda and SQS

This sample creates an API Gateway that proxies HTTP post requests onto an SQS que (InputQueue). A lambda function consumes the InputQueue, applies some processing and puts a new message on a second que (FirstInternalQueue), which a second lambda consumes. Failes processesing is put onto a dead letter queue which a separate Labda prcocesses.
