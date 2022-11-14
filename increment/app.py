import boto3
import simplejson as json


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')  
    table = dynamodb.Table('sitevisitors')
    data = table.update_item(
        Key={
            'id': '0'
        },
        ExpressionAttributeValues={':val': 1},
        UpdateExpression="set visitor_count = visitor_count + :val",
        ReturnValues="UPDATED_NEW"
    )

    return {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*', 
        'Access-Control-Allow-Methods': 'POST' 
      },
    }