# EventBridge test

Testing EventBridge triggering Lambda Function, deployed with AWS SAM.

#### Sets up

- EventBridge custom event bus
- Publish event Lambda Function that publishes onto the event bus
- 3 Lambda functions invoked when events with various event patterns are put on the bus
