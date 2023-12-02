import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('acme_products')

def lambda_handler(event, context):
    uuid = event['uuid']
    name = event['name'] if event['name'] else ''
    visible = event['visible'] if event['visible'] else '0'
    response = table.update_item(
        Key={
            'uuid': uuid
        },
        UpdateExpression='SET #nn=:newName, visible=:newVisible, updated_date=:newUpdatedDate',
        ExpressionAttributeValues={
            ':newName': name,
            ':newVisible': visible,
            ':newUpdatedDate': (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        },
        ExpressionAttributeNames={
            "#nn": "name"
        },
        ReturnValues="UPDATED_NEW"
    )
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": response
    }
