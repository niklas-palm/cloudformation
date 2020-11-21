# AWS resources

## Inventory

- `hosting.yml` sets up an S3 bucket, adds permissions for an Origin Access Identity to read from that bucket (otherwise locked down) and a CloudFront distribution to use that OAI to serve content as well as redirect all traffic to HTTPS.

- `cd-pipeline.yml`
  sets up a CodePipeline, triggered by changes in a given branch and repo in GitHub. The code is passed to CodeBuild which runs the commands specified in `"../buildspec.yml"`, in essence performing unittesting and build operations. The build artefacts are then passes to CodeDeploy which deploys them to the S3 bucket configured in `hosting.yml`.

- `template-pipeline-parameters.json` is a template file containing the parameters that need to be passed to AWS when deploying the `cd-pipeline-yml` stack above.

## Deployment instructions

1. Create a new file based on `template-pipeline-parameters.json` and enter all relevant values. Note that the Github OAuth token should remain secret, so make sure to not commit the new file. The parameters are available in plaintext through the AWS CloudFormation console however, so best practice is to use AWS Secrets Manager. Instructions to do that can be found at the releant place in `cd-pipeline.yml`.

2. Deploy static web hosting stack:

```bash
aws cloudformation deploy --template-file hosting.yml --stack-name <hosting-stack-name>
```

3. Deploy CD-pipeline stack:

```bash
aws cloudformation deploy \
--template-file cd-pipeline.yml \
--stack-name <pipeline-stack-name> \
--capabilities CAPABILITY_IAM \
--parameter-overrides file://./secret-pipeline-parameters.json
```
