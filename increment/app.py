import json

import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')  
    table = dynamodb.Table('sitevisitors')
    data = table.update_item(
        Key={
            'id': '0'
        },
        ExpressionAttributeValues={':val': 1},
        UpdateExpression="set visitor_count = visitor_count + :val"
    )
    
    return {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
    }