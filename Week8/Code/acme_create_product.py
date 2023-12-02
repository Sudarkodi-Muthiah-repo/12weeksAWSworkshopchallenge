import boto3
from datetime import datetime
from uuid import uuid4

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('acme_products')
    
def lambda_handler(event, context):
    date = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    uuid = uuid4()
    name = event['name'] if event['name'] else ''
    visible = event['visible'] if event['visible'] else '0'
    response = table.put_item(
        Item={
            'uuid': uuid.hex,
            'visible': visible,
            'name': name,
            'creation_date': date,
            'updated_date': date
        }
    )
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": response
    }
