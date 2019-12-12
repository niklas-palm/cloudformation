# CloudFormation samples

This repo contains some CloudFormation samples for creating various architectures on AWS.

## Usage

To use the templates in this repo, you can use either the AWS console or the AWS cli.

### Configure CLI

Install aws-cli with your preferred package manager.

Cli usage of these samples requires aws credentials for a "default" account stored locally inside ~./aws.

To configure with the aws-cli, Run

```bash
aws configure
```

and follow the instructions.

### Console

Simply navigate to CloudFormation in AWS console and create a new stack from a template

## Samples

All the samples in this repo are using AMIs from Oktober 2019, so manual update of the relevant AMIs in the mappings may be needed.

### /ec2_lb_web

Creates a VPC in two AZs with one public and one private subnet in each, with a loadbalancer directing trafic to an autoscaling group, where at least two instances are running.
