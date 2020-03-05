exports.lambdaHandler = event => {
  console.log(event.Records);

  event.Records.forEach(record => {
    console.log(record.dynamodb);
  });

  return;
};
