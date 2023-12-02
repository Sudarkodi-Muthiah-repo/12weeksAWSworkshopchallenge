import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('acme_products')


def lambda_handler(event, context):
    response = table.query(
        IndexName= "visible-index",
        KeyConditionExpression= "visible = :visible",
        ExpressionAttributeValues= {
            ":visible": "1"
        },
    )
    return {
        'statusCode': 200,
        "headers": {
            "Content-Type": "application/json"
        },
        'body': response
    }
