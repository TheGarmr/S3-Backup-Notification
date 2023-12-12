# S3 Backup Notification ![pipeline status](https://gitlab.honchar.net/garmr/S3_backup_notification/badges/main/pipeline.svg?ignore_skipped=true)

## Overview

This AWS Lambda function is designed to send notifications using [ntfy](https://github.com/dschep/ntfy) when the specified S3 backup bucket is updated. It can be used to alert users or monitoring systems when new files are added or modifications occur in the backup bucket.

## Setup

### 1. Requirements

- AWS Lambda configured with appropriate permissions.
- [ntfy](https://github.com/binwiederhier/ntfy) installed on your server.

### 2. Lambda Configuration

- Create a new Lambda function in the AWS Management Console.
- Configure the Lambda function with an appropriate IAM role that grants S3 read permissions and the necessary AWS Lambda permissions.
- Upload the Lambda deployment package, including your Python script and any dependencies.

### 3. Environment Variables

Configure the following environment variables for your Lambda function:

- `NTFY_BASE_URL`: The url of the NTFY server.
- `NTFY_TOPIC_NAME`: The ntfy target topic to send notifications.

### 4. Trigger Configuration

Add an S3 trigger to the Lambda function, specifying the S3 bucket and events to trigger the Lambda function (e.g., ObjectCreated events).

### 5. Used libraries
- [ntfpy](https://github.com/Nevalicjus/ntfpy) - Python API Wrapper for ntfy.sh
