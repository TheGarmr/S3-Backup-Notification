import json
import os
from ntfpy import NTFYServer, NTFYClient, NTFYPushMessage

NTFY_BASE_URL = os.environ['NTFY_BASE_URL']
NTFY_TOPIC_NAME = os.environ['NTFY_TOPIC_NAME']

def send_message(title, message):
    try:
        server = NTFYServer(NTFY_BASE_URL)
        client = NTFYClient(server, NTFY_TOPIC_NAME)
        message = NTFYPushMessage(message=message, title=title, tags=["card_index_dividers"])

        client.send_message(message)
    except Exception as e:
        print('Error while sending notification:', e)

def handle_s3_update(events, context):
    try:
        print("Received event: " + json.dumps(events, separators=(',', ':')))

        for event in events['Records']:
            bucketName = event['s3']['bucket']['name']
            objectKey = event['s3']['object']['key'].replace("%2F", "/").replace("%3A", ":")
            eventName = event['eventName']
            send_message(f"{bucketName} bucket", f"Processed {eventName} for {objectKey}")

        return { 'statusCode': 200, 'body': json.dumps('S3 event processed successfully') }
    except Exception as e:
        print('Error while sending notification:', e)
        return { 'statusCode': 500, 'body': json.dumps('S3 event processed unsuccessfully') }
