import json
import boto3

sns = boto3.client('sns')

def handler(event, context):
    for record in event['Records']:
        msg = record['body']
        sqs_message = json.loads(msg)
        bucket = sqs_message['Records'][0]['s3']['bucket']['name']
        object_key = sqs_message['Records'][0]['s3']['object']['key']
        message = {
        'bucket': bucket_name,
        'object_key': object_key
    }   
        
        response = sns.publish(
            TopicArn='arn:aws:sns:us-east-1:426857564226:sns-topic-sujata',
            Message=json.dumps({'default': message}),
            MessageStructure='json'
        )
        print(f"Published to SNS: {response}")
    return "Success"
