# CloudFormation samples

This repo contains some terraform samples for creating various architectures on AWS.

## Usage

### Configure

Usage of these samples requires aws credentials for a "default" account stored locally inside ~./aws.

To configure with the aws-cli, Run

```bash
aws configure
```

and follow the instructions.

## Samples

All the samples in this repo is using AMIs in the Ireland region.

### /ec2_lb_web

Creates a VPC in two AZs with one public and one private subnet in each, with a loadbalancer directing trafic to an autoscaling group, where at least two instances are running.
